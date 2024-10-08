# Basic Simple Data Transfer Protocol Data Structures and Sample Server
This directory contains the modules for the basic SDTP data structures and a Python server framework.  The SDTP structures are in the submodule sdtp, with the following two submodules:
1. sdtp_utils: this contains the constant type declarations and an exception thrown by the SDTP routines
2. sdtp_table. This module contains the basic SDMLTable structure, which is the basis for both client- and server-side SDTP operations.  I
3. sdtp_filter. This module contains  the SDQLFilter class, which when instantiated filters SDMLTables.  In addition, a utility `check_valid_spec` checks to ensure that a filter specification is valid

This directory also contains the modules that serve SDTP tables.  The principal module is table_server, that implements the middleware overlying a `SDMLTable` to support web services.  The principal class in table_server is `TableServer`, which implements a dictionary of Tables indexed by the table name, and supports methods which detail what tables are available under the authorization given and the schemata of those tables, what authorization is required for each table, the ability to add an SDTP table, and methods which support the construction of filters over the hosted `Table`
The `TableServer` does not work with `SDMLTable`s directly, but with a containing class here, `Table`, which adds the ability to authenticate to use a `Table`.  `Table` also offers the ability to create a `RowTable` from a JSON specification.
In addition, table_server.py implements the self-explanatory `TableNotFoundException`.
`sdtp_server` is a reference implementation of an SDTP server, implemented in Flask.  It implements all of the routes specified in the SDTP specification.  The route / and /help prints a list of the supported routes.
`app` is a thin overlay on `stdp_server`; it simply initializes the stdp server with the tables found in the directories in the `SDTP_PATH` environment variable.