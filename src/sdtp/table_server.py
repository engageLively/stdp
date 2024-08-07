'''
Middleware for a server deployment.  This is designed
to sit between the SDTP objects (in sdtp)
and a server.  These objects provide two principal
functions:
1. Keep the set of tables by name
2. Handle authentication on a table-specific basis
3. Convert results into the wire format for transmission

There are two major classes: 
1. Table, which provides a wrapper around the SDTP Table with the table's
   name, authentication requirememts, and result-conversion utilities
2. TableServer, which provides a registry and lookup service to Tables
'''

# BSD 3-Clause License

# Copyright (c) 2024, The Regents of the University of California (Regents)
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from json import load

import pandas as pd

from sdtp import InvalidDataException
from sdtp import RowTableFactory, RemoteSDMLTableFactory

class TableNotFoundException(Exception):
    '''
    An exception that is thrown when a table is not found in the TableServer
    '''

    def __init__(self, message):
        super().__init__(message)


class TableNotAuthorizedException(Exception):
    '''
    An exception that is thrown when ab attempt is made to access a table without authorization
    '''

    def __init__(self, message):
        super().__init__(message)


class ColumnNotFoundException(Exception):
    '''
    An exception that is thrown when a column is not found for a specific table
    '''

    def __init__(self, message):
        super().__init__(message)


def _check_headers(headers):
    '''
    Each header should be a dictionary of the form variable:  value,
    both of which must <string>, which
    are the authorization tokens required to access this table.  Doesn't return  a value: raises an error if a header isn't compliant
    '''
    assert isinstance(headers, dict), f'Headers must be a dictionary, not {type(headers)}'
    for header in headers.items():
        assert isinstance(header[0], str), f'Header key must be a string, not {type(header[0])}'
        assert type(header[1]) in {int, str,
                                   bool}, f'Header value must be a string, int, or boolean,  not {type(header[1])}'


class Table:
    '''
    A SDMLTable with authorization information.  This is what is
    stored in the TableServer; conceptually, it is a pair, (table, headers) where table is a SDMLTable and headers is a dictionary
    of variables and values used to access the data.  raises an InvalidDataException if:
    (1) The table is not a SDMLTable
    (2) header_dict is not a dictionary
    (3) A key in header-dict is not a string
    (4) A value in header-dict is not one of <int, str, bool>
    Arguments:
         table: the table to be stored
         header_dict: a dictionary of the form {variable: value} used to access the table
    '''

    def __init__(self, table, header_dict={}):
        invalid_error = InvalidDataException('The table parameter to Table must be a SDMLTable')
        try:
            if not table.is_sdtp_table:
                raise invalid_error
        except AttributeError:
            raise invalid_error
        if header_dict is None: header_dict = {}
        try:
            _check_headers(header_dict)
        except AssertionError as err:
            raise InvalidDataException(err)

        self.table = table
        self.header_dict = header_dict

    def authorized(self, headers={}):
        '''
        Return True iff the provided dictionary of headers contains the
        right variables and values to access this table
        Arguments:
            headers: A dictionary of the form {variable: value} containing the provided headers
        '''
        # Make sure we don't have None passed in
        if headers is None: headers = {}
        # Just check for each value.  use get() rather than direct
        # reference to avoid KeyError, and note that if the item isn't
        # there None won't be equal to item[1]
        for item in self.header_dict.items():
            provided_value = headers.get(item[0])
            if provided_value != item[1]: return False
        # Everything matched!
        return True

    def auth_variables(self):
        '''
        Return the list of variables required for authorization, but
        not their values
        Returns:
        list of variable names required for authorization,
        '''
        return list(self.header_dict.keys())


    

def _check_type(value, type, message_prefix):
    assert isinstance(value, type), f'{message_prefix} {type(value)}'

def _check_dict_and_keys(dictionary, keys, dict_message, dict_name):
    _check_type(dictionary, dict, dict_message)
    missing_keys = keys - dictionary.keys()
    assert len(missing_keys) == 0, f'{dict_name} is missing keys {missing_keys}'



def _check_table_spec(table_spec):
    # Make sure a table_spec is a dictionary with two entries, a name and a table,
    # and the type of name is a string and the type of table is a Table
    _check_dict_and_keys(table_spec, {'name', 'table'}, 'table_spec must be a dictionary not', 'table_spec')
    _check_type(table_spec["name"], str, 'The name in table_spec must be a string, not')
    _check_type(table_spec["table"], Table, 'The table in table_spec must be a Table, not')

def _check_valid_form(table_form):
    # Make sure a table_form is a dictionary with two entries, a name and a table,
    # and the type of name is a string, the type of table is a dictionary, and the 
    # table dictionary contains fields schema and type
    _check_dict_and_keys(table_form, {'name', 'table'}, 'table_form must be a dictionary not', 'table_form')
    _check_type(table_form["name"], str, 'The name in table_form must be a string, not')
    _check_dict_and_keys(table_form['table'], {'type', 'schema'}, 'table_form["table"] must be a dictionary not', 'table_form')



class TableServer:
    '''
    The server for tables.  Its task is to maintain a correspondence
    between table names and the actual tables.  It also maintains the security information for a table (the variables and values required to access the table), and gives column information across tables
    '''

    # Conceptually, there is only a single TableServer  (why would there #  be more?), and so this could be in a global variable and its # methods global.
    def __init__(self):
        self.servers = {}
        self.factories = {}
        # factories which are part of the standard  distribution
        self.add_table_factory('RowTable', RowTableFactory())
        self.add_table_factory('RemoteSDMLTable', RemoteSDMLTableFactory())


    def add_table_factory(self, table_type, table_factory):
        '''
        Add a TableFactory for table type table_type.  When 
        self.add_table_from_dictionary(table_spec) is called, the appropriate 
        factory is called to build it
        Arguments:
           table_type: a string indicating the table type
           table_factory: an instance of a subclass of TableFactory which actually builds the table
        '''
        self.factories[table_type] = table_factory

    def get_table_dictionary(self, headers={}):
        '''
        Get the schemas tables authorized with headers as a dictionary
        {table_name: table}

        Returns:
            a dictionary of the schemata the authorized tables by name
        '''
        result = {}
        if headers is None: headers = {}

        for items in self.servers.items():
            if items[1].authorized(headers):
                result[items[0]] = items[1].table.schema
        return result

    def get_auth_spec(self):
        '''
        Return a dictionary of the names of the tables and the authorization variables required for head
        Returns:
        a Dictionary with key table_name and values the names of the variables required for that table
        '''
        result = {}
        for items in self.servers.items():
            result[items[0]] = items[1].auth_variables()
        return result

    def get_all_tables(self, headers={}):
        '''
        Get all the tables.  This
        is to support a request for a numeric_spec or all_values for a column name when the
        table_name is not specified. In this case, all tables will be searched for this column name.
        Arguments: the dictionary of headers

        Returns:
            a list of all tables which are authorized by the headers
        '''
        servers = self.servers.values()
        return [server.table for server in servers if server.authorized(headers)]

    def add_sdtp_table(self, table_spec):
        '''
        Register a SDMLTable to serve data for a specific table name.
        Raises an InvalidDataException if table_name is None or sdtp_table is None or is not an instance of SDMLTable.

        Arguments:
            table_spec: dictionary of the form {"name", "table"}, where table is a Table (see above)

        '''
        _check_table_spec(table_spec)
        self.servers[table_spec["name"]] = table_spec["table"]


    def add_sdtp_table_from_dictionary(self, table_dictionary):
        '''
        Add an  SDMLTable from a dictionary (intermediate on-disk form).  The intermediate form has
        a name and a table dictionary.  The table dictionary has fields schema and type, and then type-
        specific fields.  Calls self.factories[table_dictionary["table"]["type"]] to build the table,
        then calls self.add_sdtp_table to add the table.
        Raises an InvalidDataException if self.add_table_spec raises it or if the factory 
        is not present, or if the factory raises an exception

        Arguments:
            table_dictionary: dictionary of the form {"name", "table"}, where table is a table specification: a dictionary
                             with the fields type and schema

        '''
        _check_valid_form(table_dictionary)
        name = table_dictionary['name']
        table_dict = table_dictionary['table']
        table_type = table_dict['type']
        if table_type in self.factories.keys():
            table = self.factories[table_type].build_table(table_dict)
            self.add_sdtp_table({"name": name, "table": Table(table)})
        else:
            raise InvalidDataException(f'No factory registered for {table_type}')

    def get_table(self, table_name, headers={}):
        '''
        Get the table with name table_name, first checking to see
        if  table access is authorized by the passed headers.
        Arguments:
            table_name: name of the table to search for
            headers: dictionary of header variables and values
        Returns:
            The SDTP table corresponding to the request
        Raises:
            TableNotFoundException if the table is not found
            TableNotAuthorizedException if access to the table is not authorized
        '''
        try:
            server = self.servers[table_name]
            if server.authorized(headers):
                return server.table
            else:
                raise TableNotAuthorizedException(f'Access to table {table_name} not authorized')
        except KeyError:
            raise TableNotFoundException(f'Table {table_name} not found')

    def get_all_values(self, table_name, column_name, headers={}):
        '''
        Get all of the distinct values for column column_name for table
        table_name.  Returns the list of distinct values for the columns
        Arguments:
            table_name: table to be searched
            column_name: name of the column
            headers: headers to check for authorization
        Returns:
            Returns the list of distinct values for the columns
        Raises:
            TableNotFoundException if the table is not found
            TableNotAuthorizedException if access to the table is not authorized
            ColumnNotFoundException if the column can't be found
        '''

        _check_type(column_name, str, 'Column name must be a string, not')
        table = self.get_table(table_name,
                               headers)  # Note this will throw the TableNotFound and TableNotAuthorizedException

        try:
            return table.all_values(column_name)
        except InvalidDataException:
            raise ColumnNotFoundException(f'Column {column_name} not found in table {table_name}')

    def get_range_spec(self, table_name, column_name, headers={}):
        '''
        Get the range specification for column column_name for table
        table_name.  Returns  a dictionary with keys{max_val, min_val}
        Arguments:
            table_name: table to be searched
            column_name: name of the column
            headers: headers to check for authorization
        Returns:
            Returns  a dictionary with keys{max_val, min_val}
        Raises:
            TableNotFoundException if the table is not found
            TableNotAuthorizedException if access to the table is not authorized
            ColumnNotFoundException if the column can't be found
        '''
        _check_type(column_name, str, 'Column name must be a string, not')
        table = self.get_table(table_name,
                               headers)  # Note this will throw the TableNotFound and TableNotAuthorizedException
        try:
            return table.range_spec(column_name)
        except InvalidDataException:
            raise ColumnNotFoundException(f'Column {column_name} not found in table {table_name}')
        


