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
import datetime
import random
import re
import pprint
import string
from table_data_good import names, ages, dates, datetimes, times, booleans, series_for_name
'''
This generates the tests/filter_tests.py file, which is used to test  the primitive (IN_LIST, IN_RANGE, REGEX_MATCH)
filters of the DataPlane.  A test is a pair (filter_spec, expected_indices) and this code
generates a large set of those pairs  which are then used by the tester to do the actual tests.
The test is just instantiating the filter from the spec, running the filter on the table formed
from the series in table_data_good.py
'''

# The name is the name of the column in the table, the value is the series which formes the
# column

series_for_name = {'name': names, 'age': ages, 'date': dates, 'time': times,
                   'datetime': datetimes, 'boolean': booleans}


def _get_indices_for_range(series, min_val, max_val):
    # Matches an IN_RANGE.  Returns the indices in series where the value is between min_val and max_val inclusive
    return set([i for i in range(len(series)) if series[i] >= min_val and series[i] <= max_val])

def _get_indices_for_in_list(series, value_list):
     # Matches an IN_LIST filter.  Returns the indices in series where the value appears in value_list
    return set([i for i in range(len(series)) if series[i] in value_list])

def _get_indices_for_regex(series, expression):
    # Matches a REGEX_MATCH filter.  Returns the indices in series which fully match re
    regex = re.compile(expression)
    return set([i for i in range(len(series)) if regex.fullmatch(series[i])])


def make_in_range_test(column, min_val, max_val):
    '''
    Make a range filter spec from column name, min_val, and max_val, and then
    find the indicies that the actual filter is expected to return
    Parameters:
        column: name of the column
        max_val: maximum value for the filter
        min_val: minimum value for the filter
    Returns:
        An object with fields spec, the spec to be turned into the filter, and expected,
        the row indices with entries in the series associated with the column whose value is between min_val and max_val
        between min_val and max_val

    '''
    expected = _get_indices_for_range(series_for_name[column], min_val, max_val)
    return {
        "spec": {"operator": "IN_RANGE", "column": column, "max_val": max_val, "min_val": min_val},
        "expected": expected
    }

def make_in_list_test(column, values):
    '''
    Make a list filter spec from column name, values, and then
    find the indicies that the actual filter is expected to return
    Parameters:
        column: name of the column
        values: list of values to be searched

    Returns:
        An object with fields spec, the spec to be turned into the filter, and expected,
        the row indices with entries in the series associated with the column whose value is
        in values

    '''
    expected = _get_indices_for_in_list(series_for_name[column], values)
    return {
        "spec": {"operator": "IN_LIST", "column": column, "values": values},
        "expected": expected
    }

def make_regex_test(column, expression):
    '''
    Make a regex filter spec from column name, expresison, and then
    find the indicies that the actual filter is expected to return
    Parameters:
        column: name of the column
        expression: expression to be matched

    Returns:
        An object with fields spec, the spec to be turned into the filter, and expected,
        the row indices with entries in the series associated with the column which do a fullmatch
        with expression
    '''
    expected = _get_indices_for_regex(series_for_name[column], expression)
    return {
        "spec": {"operator": "REGEX_MATCH", "column": column, "expression": expression},
        "expected": expected
    }

def generate_in_range_test(column):
    '''
    Generate a random in_range test for column, picking out two elements at random
    for the max_val and min_val, and then using make_in_range_test to generate the test
    Parameters:
        column: the name of the column to generate the test for
    Returns
        The test in the form generated by make_in_range_test
    '''
    series = series_for_name[column]
    elements = random.choices(series, k=2)
    return make_in_range_test(column, min(elements), max(elements))

def generate_in_list_test(column):
    '''
    Generate a random in_list test for column, picking out n  elements at random
    for the value list, and then using make_in_list_test to generate the test
    Parameters:
        column: the name of the column to generate the test for
    Returns
        The test in the form generated by make_in_list_test
    '''
    series = series_for_name[column]
    num_elements = random.randrange(0, len(series))
    elements = random.choices(series, k=num_elements)
    return make_in_list_test(column, elements)

def generate_regex_test(column):
    '''
    Generate a random regex test for column, picking out an  element at random
    and simply changing the first and last letter to .*, and then using make_regex_test to generate the test.
    If it's only two  letters long, changes the first letter to .* and appends .*, and
    it if's only one letter long, appends and prepends .*
    Parameters:
        column: the name of the column to generate the test for
    Returns
        The test in the form generated by make_regex_test
    '''
    series = series_for_name[column]
    seed = random.choice(series)
    expression = f'.*{seed[1:len(seed) - 2]}.*' if len(seed) > 2 else f'*.{seed[1:]}.*' if len(seed) > 1 else f'.*{seed}.*'
    return make_regex_test(column, expression)

def generate_all_in_range_tests():
    '''
    Generate all the in range tests.  For each column, generate the edge cases
    (min and max of the column, and then the case where the min and max are identical),
    then choose a bunch of random cases
    Returns:
        a list of tests generated by make_in_range_test
    '''
    columns = series_for_name.keys()
    result = []
    for column in columns:
        series = series_for_name[column]
        series_min = min(series)
        series_max = max(series)
        result.append(make_in_range_test(column, series_min, series_max))
        result.append(make_in_range_test(column, series_max, series_max))
        result.append(make_in_range_test(column, series_min, series_min))
        rand_tests = random.randrange(1, 20)
        for i in range(rand_tests):
            result.append(generate_in_range_test(column))
    return result

def generate_all_in_list_tests():
    '''
    Generate all the in list tests.  For each column, generate the edge cases
    (value list is the entire column, value list is empty),
    then choose a bunch of random cases
    Returns:
        a list of tests generated by make_in_list_test
    '''
    columns = series_for_name.keys()
    result = []
    for column in columns:
        series = series_for_name[column]
        result.append(make_in_list_test(column, []))
        result.append(make_in_list_test(column, series))
        rand_tests = random.randrange(1, 20)
        for i in range(rand_tests):
            result.append(generate_in_range_test(column))
    return result

def generate_all_regex_tests():
    '''
    Generate all the regex tests.  These are only over column names, since the
    required column type is STRING.  Generate the edge cases
    (expression is empty, expression is .*, expression is <l>.* expresson .*<l> where l
    i sany letter), then choose a bunch of random cases
    Returns:
        a list of tests generated by make_regex_test
    '''
    result = []

    expressions = ['', '.*'] + [f'{c}.*' for c in string.ascii_letters] + [f'.*{c}' for c in string.ascii_letters]
    result = [make_regex_test('name', expression) for expression in expressions]
    rand_tests = random.randrange(1, 20)
    for i in range(rand_tests):
        result.append(generate_in_range_test('name'))
    return result

# Use the above routines to generate all the tests
tests = {
    'in_range': generate_all_in_range_tests(),
    'in_list': generate_all_in_list_tests(),
    'regex_match': generate_all_regex_tests()
}


# Pretty print the tests on tests/filter_tests.py, so they can be read in by the tester
with open('tests/filter_tests.py', 'w') as f:
    f.writeln('import datetime')
    f.writeln("'''")
    f.writeln("This file is auto-generated, do not change.  The source code to generate this file is in")
    f.writelin("generate_tests.py.  Modify the code there.")
    f.writeln("'''")
    f.write('filter_tests = ')
    pprint.pprint(tests, f, compact = True, width = 80)


