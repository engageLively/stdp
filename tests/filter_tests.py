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

filter_tests = {
  'in_list': [
    {
      'expected': set(),
      'spec': {'column': 'name', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'name', 'operator': 'IN_LIST', 'values': ['Pearla', 'Karleen', 'Bathsheba', 'Casi', 'Gusti', 'Anastassia', 'Nonah', 'Janine', 'Nicki', 'Noemi', 'Vivyanne', 'Jeanne', 'Carina', 'Ivy', 'Jenine', 'Tandie', 'Abbe', 'Laney', 'Shandeigh', 'Aarika', 'Caria', 'Jorrie', 'Maisey', 'Shani', 'Casi', 'Ashley', 'Roselia', 'Petronia', 'Brandice', 'Debi', 'Andee', 'Teodora', 'Neysa', 'Beverley', 'Rey', 'Brittni', 'Rheba', 'Jeanna', 'Lyssa', 'Elayne', 'Magdalene', 'Violante', 'Netta', 'Virginia', 'Natalie', 'Mildred', 'Ophelia', 'Alma', 'Lettie', 'Catherina', 'Philipa', 'Marget', 'Karol', 'Berget', 'Doloritas', 'Kessia', 'Jaynell', 'Bethanne', 'Mildred', 'Gustie', 'Irina', 'Felipa', 'Charlean', 'Jaquelin', 'Isadora', 'Jelene', 'Benedicta', 'Piper', 'Almeria', 'Editha', 'Deena', 'Celestyn', 'Betsy', 'Georgianna', 'Jacklin', 'Georgiana', 'Robby', 'Emmalyn', 'Robinett', 'Nickie', 'Jo-Ann', 'Rosita', 'Ingrid', 'Erminie', 'Tami', 'Meg', 'Devan', 'Annaliese', 'Ginevra', 'Wilmette', 'Imogen', 'Melony', 'Kalli', 'Tessy', 'Lesly', 'Deedee', 'Mellisent', 'Perl', 'Milzie', 'Allegra']}
    },
    {
      'expected': {1, 7, 8, 9, 11, 13, 14, 17, 21, 22, 32, 37, 38, 40, 42, 44, 45, 48, 51, 52, 55, 56, 58, 60, 63, 64, 65, 74, 79, 80, 85, 91, 92, 94, 96, 98},
      'spec': {'column': 'name', 'max_val': 'Noemi', 'min_val': 'Irina', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {3, 35, 71, 12, 49, 20, 24, 28},
      'spec': {'column': 'name', 'max_val': 'Celestyn', 'min_val': 'Brandice', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 29, 31, 32, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 50, 51, 52, 54, 55, 56, 58, 59, 60, 61, 63, 64, 65, 67, 69, 70, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98},
      'spec': {'column': 'name', 'max_val': 'Wilmette', 'min_val': 'Debi', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 6, 8, 9, 17, 21, 22, 27, 32, 34, 36, 38, 40, 42, 44, 45, 46, 48, 50, 51, 52, 55, 58, 67, 76, 79, 85, 91, 92, 94, 96, 97, 98},
      'spec': {'column': 'name', 'max_val': 'Robby', 'min_val': 'Jorrie', 'operator': 'IN_RANGE'}
    },
    {
      'expected': set(),
      'spec': {'column': 'age', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'age', 'operator': 'IN_LIST', 'values': [64, 78, 79, 13, 28, 70, 79, 87, 31, 7, 46, 51, 29, 13, 43, 17, 83, 29, 46, 55, 60, 37, 50, 9, 57, 88, 74, 47, 67, 42, 82, 63, 79, 81, 34, 77, 80, 51, 68, 61, 72, 71, 59, 55, 31, 57, 31, 66, 91, 45, 58, 59, 77, 15, 42, 39, 92, 82, 90, 77, 60, 20, 23, 31, 83, 34, 89, 83, 55, 38, 45, 51, 10, 90, 55, 85, 38, 53, 75, 11, 74, 80, 52, 31, 69, 25, 76, 63, 11, 77, 33, 18, 19, 53, 64, 11, 17, 50, 92, 55]}
    },
    {
      'expected': {0, 11, 19, 20, 22, 24, 31, 37, 39, 42, 43, 45, 50, 51, 60, 68, 71, 74, 77, 82, 87, 93, 94, 97, 99},
      'spec': {'column': 'age', 'max_val': 64, 'min_val': 50, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 5, 6, 19, 20, 24, 26, 28, 30, 31, 32, 33, 35, 36, 38, 39, 40, 41, 42, 43, 45, 47, 50, 51, 52, 57, 59, 60, 68, 74, 78, 80, 81, 84, 86, 87, 89, 94, 99},
      'spec': {'column': 'age', 'max_val': 82, 'min_val': 55, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {11, 19, 24, 37, 42, 43, 45, 50, 51, 68, 71, 74, 77, 82, 93, 99},
      'spec': {'column': 'age', 'max_val': 59, 'min_val': 51, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {8, 10, 11, 14, 18, 19, 21, 22, 27, 29, 34, 37, 43, 44, 46, 49, 54, 55, 63, 65, 68, 69, 70, 71, 74, 76, 77, 82, 83, 90, 93, 97, 99},
      'spec': {'column': 'age', 'max_val': 55, 'min_val': 31, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {3, 4, 8, 12, 13, 15, 17, 21, 29, 34, 44, 46, 53, 54, 55, 61, 62, 63, 65, 69, 76, 79, 83, 85, 88, 90, 91, 92, 95, 96},
      'spec': {'column': 'age', 'max_val': 42, 'min_val': 11, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 6, 7, 16, 25, 30, 32, 33, 35, 36, 52, 57, 58, 59, 64, 66, 67, 73, 75, 81, 89},
      'spec': {'column': 'age', 'max_val': 90, 'min_val': 77, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 5, 26, 28, 35, 38, 40, 41, 47, 52, 59, 78, 80, 84, 86, 89, 94},
      'spec': {'column': 'age', 'max_val': 77, 'min_val': 64, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 5, 10, 11, 18, 19, 20, 22, 24, 27, 28, 31, 37, 38, 39, 42, 43, 45, 47, 50, 51, 60, 68, 71, 74, 77, 82, 84, 87, 93, 94, 97, 99},
      'spec': {'column': 'age', 'max_val': 70, 'min_val': 46, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {64, 66, 67, 98, 7, 73, 75, 16, 48, 56, 25, 58},
      'spec': {'column': 'age', 'max_val': 92, 'min_val': 83, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {35, 78, 80, 52, 86, 89, 26, 59},
      'spec': {'column': 'age', 'max_val': 77, 'min_val': 74, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 8, 12, 14, 17, 21, 29, 34, 44, 46, 49, 54, 55, 61, 62, 63, 65, 69, 70, 76, 83, 85, 90, 91, 92},
      'spec': {'column': 'age', 'max_val': 45, 'min_val': 18, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 5, 11, 19, 20, 24, 26, 28, 31, 35, 37, 38, 39, 40, 41, 42, 43, 45, 47, 50, 51, 52, 59, 60, 68, 71, 74, 77, 78, 80, 82, 84, 86, 87, 89, 93, 94, 99},
      'spec': {'column': 'age', 'max_val': 77, 'min_val': 51, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 3, 4, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 24, 27, 28, 29, 31, 34, 37, 38, 39, 42, 43, 44, 45, 46, 47, 49, 50, 51, 53, 54, 55, 60, 61, 62, 63, 65, 68, 69, 70, 71, 74, 76, 77, 79, 82, 83, 85, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99},
      'spec': {'column': 'age', 'max_val': 68, 'min_val': 11, 'operator': 'IN_RANGE'}
    },
    {
      'expected': set(),
      'spec': {'column': 'date', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'date', 'operator': 'IN_LIST', 'values': [datetime.date(2020, 9, 24), datetime.date(2011, 12, 9), datetime.date(2010, 8, 7), datetime.date(2021, 10, 17), datetime.date(2013, 7, 4), datetime.date(2022, 7, 8), datetime.date(2013, 6, 20), datetime.date(2019, 12, 17), datetime.date(2005, 7, 25), datetime.date(2000, 12, 26), datetime.date(2003, 2, 23), datetime.date(2007, 11, 11), datetime.date(2017, 5, 23), datetime.date(2022, 10, 24), datetime.date(2017, 7, 1), datetime.date(2010, 6, 28), datetime.date(2009, 7, 23), datetime.date(2005, 6, 8), datetime.date(2001, 1, 7), datetime.date(2005, 5, 27), datetime.date(2010, 3, 19), datetime.date(2013, 10, 12), datetime.date(2007, 10, 9), datetime.date(2006, 11, 11), datetime.date(2018, 3, 11), datetime.date(2016, 12, 14), datetime.date(2000, 7, 5), datetime.date(2015, 3, 5), datetime.date(2004, 8, 31), datetime.date(2001, 4, 14), datetime.date(2006, 2, 2), datetime.date(2021, 10, 2), datetime.date(2014, 1, 6), datetime.date(2003, 12, 17), datetime.date(2019, 7, 26), datetime.date(2008, 4, 19), datetime.date(2019, 6, 8), datetime.date(2010, 10, 2), datetime.date(2021, 6, 11), datetime.date(2015, 6, 16), datetime.date(2005, 4, 1), datetime.date(2004, 4, 21), datetime.date(2021, 2, 10), datetime.date(2019, 9, 28), datetime.date(2020, 4, 2), datetime.date(2004, 9, 28), datetime.date(2008, 4, 22), datetime.date(2001, 1, 22), datetime.date(2014, 8, 15), datetime.date(2016, 1, 18), datetime.date(2014, 4, 29), datetime.date(2002, 6, 11), datetime.date(2015, 10, 28), datetime.date(2020, 7, 22), datetime.date(2015, 5, 17), datetime.date(2019, 3, 23), datetime.date(2023, 1, 24), datetime.date(2017, 7, 22), datetime.date(2021, 4, 21), datetime.date(2006, 1, 4), datetime.date(2020, 2, 11), datetime.date(2018, 12, 1), datetime.date(2021, 6, 22), datetime.date(2001, 11, 28), datetime.date(2015, 4, 5), datetime.date(2010, 12, 10), datetime.date(2011, 3, 27), datetime.date(2012, 10, 13), datetime.date(2003, 5, 29), datetime.date(2016, 7, 23), datetime.date(2004, 5, 23), datetime.date(2022, 5, 28), datetime.date(2007, 8, 5), datetime.date(2007, 10, 3), datetime.date(2013, 10, 10), datetime.date(2017, 12, 17), datetime.date(2010, 12, 24), datetime.date(2003, 8, 27), datetime.date(2004, 3, 5), datetime.date(2016, 8, 27), datetime.date(2003, 4, 9), datetime.date(2013, 10, 15), datetime.date(2005, 7, 26), datetime.date(2014, 5, 21), datetime.date(2000, 3, 1), datetime.date(2018, 3, 10), datetime.date(2017, 11, 19), datetime.date(2014, 8, 13), datetime.date(2006, 7, 11), datetime.date(2010, 4, 24), datetime.date(2010, 9, 23), datetime.date(2022, 4, 1), datetime.date(2020, 6, 29), datetime.date(2003, 9, 9), datetime.date(2008, 1, 4), datetime.date(2019, 9, 3), datetime.date(2004, 12, 14), datetime.date(2016, 5, 26), datetime.date(2001, 3, 5), datetime.date(2013, 10, 3)]}
    },
    {
      'expected': set(),
      'spec': {'column': 'boolean', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'operator': 'IN_LIST', 'values': [True, True, True, True, False, False, True, False, True, True, False, True, True, True, True, True, False, True, True, True, False, True, False, False, True, False, True, True, True, False, True, True, True, True, False, False, True, True, False, True, False, False, False, True, False, False, True, True, True, False, True, True, False, False, False, True, True, False, True, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, True, True, True, True, False, True, True, False, True, False, False, False, False, False, False, False, True, True, False, False, True, True, False, True, True, False]}
    },
  ],
  "in_range": [
    {
      'expected': {8, 17, 19, 23, 28, 30, 33, 40, 41, 45, 59, 68, 70, 77, 78, 82, 88, 93, 96},
      'spec': {'column': 'date', 'max_val': datetime.date(2006, 11, 11), 'min_val': datetime.date(2003, 5, 29), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 8, 11, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 30, 32, 35, 37, 39, 40, 41, 45, 46, 48, 49, 50, 52, 54, 59, 64, 65, 66, 67, 70, 72, 73, 74, 76, 81, 82, 83, 87, 88, 89, 90, 94, 96, 97, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2016, 5, 26), 'min_val': datetime.date(2004, 4, 21), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 11, 15, 16, 20, 21, 22, 27, 32, 35, 37, 46, 48, 50, 65, 66, 67, 73, 74, 76, 81, 83, 87, 89, 90, 94, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2015, 3, 5), 'min_val': datetime.date(2007, 10, 3), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {34, 36, 7, 43, 44, 60, 95},
      'spec': {'column': 'date', 'max_val': datetime.date(2020, 4, 2), 'min_val': datetime.date(2019, 6, 8), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {8, 11, 16, 17, 19, 20, 22, 23, 28, 30, 35, 40, 45, 46, 59, 72, 73, 82, 88, 94, 96},
      'spec': {'column': 'date', 'max_val': datetime.date(2010, 3, 19), 'min_val': datetime.date(2004, 8, 31), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 69, 70, 72, 73, 74, 75, 76, 79, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95, 96, 97, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2022, 4, 1), 'min_val': datetime.date(2004, 5, 23), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {8, 72, 73, 82, 22, 23, 88, 59, 30},
      'spec': {'column': 'date', 'max_val': datetime.date(2007, 10, 9), 'min_val': datetime.date(2005, 7, 25), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 7, 12, 14, 21, 24, 25, 27, 32, 34, 36, 38, 39, 42, 43, 44, 48, 49, 50, 52, 53, 54, 55, 57, 58, 60, 61, 64, 69, 74, 75, 79, 81, 83, 85, 86, 87, 92, 95, 97, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2021, 6, 11), 'min_val': datetime.date(2013, 10, 3), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 8, 11, 15, 16, 17, 19, 20, 21, 22, 23, 28, 30, 33, 35, 37, 40, 41, 45, 46, 59, 65, 66, 67, 70, 72, 73, 74, 76, 78, 82, 88, 89, 90, 94, 96, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2013, 10, 12), 'min_val': datetime.date(2003, 12, 17), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {13, 91, 5, 71},
      'spec': {'column': 'date', 'max_val': datetime.date(2022, 10, 24), 'min_val': datetime.date(2022, 4, 1), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 4, 6, 7, 12, 14, 21, 24, 25, 27, 32, 34, 36, 39, 43, 44, 48, 49, 50, 52, 54, 55, 57, 60, 61, 64, 67, 69, 74, 75, 79, 81, 83, 85, 86, 87, 95, 97, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2020, 4, 2), 'min_val': datetime.date(2011, 12, 9), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 22, 23, 26, 28, 29, 30, 33, 35, 37, 40, 41, 45, 46, 47, 51, 59, 63, 65, 66, 67, 68, 70, 72, 73, 74, 76, 77, 78, 80, 82, 88, 89, 90, 93, 94, 96, 98, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2013, 10, 10), 'min_val': datetime.date(2000, 7, 5), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {96, 33, 70, 40, 41, 45, 78, 28, 93},
      'spec': {'column': 'date', 'max_val': datetime.date(2005, 4, 1), 'min_val': datetime.date(2003, 9, 9), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 4, 6, 21, 27, 32, 48, 50, 64, 66, 67, 74, 81, 83, 87, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2015, 4, 5), 'min_val': datetime.date(2011, 3, 27), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 4, 6, 12, 21, 25, 27, 32, 39, 48, 49, 50, 52, 54, 64, 66, 67, 69, 74, 79, 81, 83, 87, 97, 99},
      'spec': {'column': 'date', 'max_val': datetime.date(2017, 5, 23), 'min_val': datetime.date(2011, 3, 27), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 44, 92, 53, 60},
      'spec': {'column': 'date', 'max_val': datetime.date(2020, 9, 24), 'min_val': datetime.date(2020, 2, 11), 'operator': 'IN_RANGE'}
    },
    {
      'expected': set(),
      'spec': {'column': 'time', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'time', 'operator': 'IN_LIST', 'values': [datetime.time(11, 24, 55), datetime.time(13, 40, 27), datetime.time(23, 44, 12), datetime.time(17, 13, 2), datetime.time(10, 48, 5), datetime.time(17, 12), datetime.time(0, 53, 3), datetime.time(12, 19, 43), datetime.time(7, 33, 45), datetime.time(1, 6, 34), datetime.time(14, 41, 46), datetime.time(20, 21, 12), datetime.time(20, 55, 33), datetime.time(12, 36, 15), datetime.time(10, 57, 56), datetime.time(6, 38, 17), datetime.time(6, 58, 34), datetime.time(4, 7, 44), datetime.time(17, 38, 14), datetime.time(17, 35, 48), datetime.time(4, 40, 59), datetime.time(15, 9, 38), datetime.time(21, 23, 29), datetime.time(21, 59, 19), datetime.time(0, 13, 53), datetime.time(17, 30, 14), datetime.time(14, 40, 38), datetime.time(22, 40, 39), datetime.time(3, 13, 27), datetime.time(8, 19, 40), datetime.time(20, 24, 1), datetime.time(22, 20, 4), datetime.time(17, 42, 39), datetime.time(23, 15, 20), datetime.time(3, 20, 46), datetime.time(20, 25, 31), datetime.time(16, 42, 31), datetime.time(22, 15, 59), datetime.time(0, 37, 44), datetime.time(1, 46, 17), datetime.time(0, 24, 1), datetime.time(18, 54, 22), datetime.time(3, 24, 24), datetime.time(22, 17, 8), datetime.time(22, 17, 17), datetime.time(18, 28, 49), datetime.time(9, 15, 21), datetime.time(16, 55, 20), datetime.time(18, 14, 10), datetime.time(0, 11, 37), datetime.time(0, 44, 46), datetime.time(10, 9, 12), datetime.time(10, 43, 15), datetime.time(11, 16, 57), datetime.time(14, 25, 31), datetime.time(14, 6, 35), datetime.time(16, 14, 38), datetime.time(8, 58, 6), datetime.time(23, 15, 27), datetime.time(10, 7, 34), datetime.time(4, 39, 45), datetime.time(20, 3, 52), datetime.time(21, 46, 58), datetime.time(13, 24, 37), datetime.time(1, 56, 52), datetime.time(8, 9, 9), datetime.time(10, 51, 3), datetime.time(19, 19, 52), datetime.time(12, 3, 4), datetime.time(6, 11, 21), datetime.time(16, 1, 11), datetime.time(7, 9, 58), datetime.time(16, 9, 3), datetime.time(14, 7, 44), datetime.time(17, 53, 11), datetime.time(23, 35, 29), datetime.time(11, 29, 53), datetime.time(15, 53, 20), datetime.time(8, 6, 15), datetime.time(9, 23, 28), datetime.time(21, 35, 58), datetime.time(23, 11, 13), datetime.time(20, 21, 17), datetime.time(17, 47, 27), datetime.time(19, 58, 11), datetime.time(22, 28, 52), datetime.time(15, 24, 8), datetime.time(12, 33, 26), datetime.time(14, 29, 36), datetime.time(3, 35, 48), datetime.time(18, 35, 37), datetime.time(11, 52, 44), datetime.time(21, 15, 48), datetime.time(7, 39), datetime.time(4, 34, 48), datetime.time(5, 20, 58), datetime.time(18, 36, 56), datetime.time(0, 16, 33), datetime.time(7, 27, 51), datetime.time(0, 50, 14)]}
    },
    {
      'expected': {0, 1, 68, 7, 73, 76, 13, 54, 55, 87, 91, 63},
      'spec': {'column': 'time', 'max_val': datetime.time(14, 25, 31), 'min_val': datetime.time(11, 24, 55), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {3, 18, 19, 25, 32, 41, 45, 48, 67, 74, 83, 84, 90, 96},
      'spec': {'column': 'time', 'max_val': datetime.time(19, 58, 11), 'min_val': datetime.time(17, 13, 2), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 4, 7, 8, 13, 14, 15, 16, 17, 20, 28, 29, 34, 39, 42, 46, 51, 52, 53, 57, 59, 60, 64, 65, 66, 68, 69, 71, 76, 78, 79, 87, 89, 91, 93, 94, 95, 98},
      'spec': {'column': 'time', 'max_val': datetime.time(12, 36, 15), 'min_val': datetime.time(1, 46, 17), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {64, 34, 42, 17, 89, 28},
      'spec': {'column': 'time', 'max_val': datetime.time(4, 7, 44), 'min_val': datetime.time(1, 56, 52), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {10, 77, 21, 54, 86, 88, 26},
      'spec': {'column': 'time', 'max_val': datetime.time(15, 53, 20), 'min_val': datetime.time(14, 25, 31), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {64, 34, 39, 9, 42, 60, 17, 20, 89, 28, 94, 95},
      'spec': {'column': 'time', 'max_val': datetime.time(5, 20, 58), 'min_val': datetime.time(1, 6, 34), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 4, 14, 29, 46, 51, 52, 53, 57, 59, 65, 66, 76, 78, 79},
      'spec': {'column': 'time', 'max_val': datetime.time(11, 29, 53), 'min_val': datetime.time(8, 6, 15), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 6, 8, 9, 15, 16, 17, 20, 28, 29, 34, 39, 42, 46, 50, 51, 52, 57, 59, 60, 64, 65, 66, 69, 71, 78, 79, 89, 93, 94, 95, 98, 99},
      'spec': {'column': 'time', 'max_val': datetime.time(10, 51, 3), 'min_val': datetime.time(0, 44, 46), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 4, 6, 8, 9, 14, 15, 16, 17, 20, 24, 28, 29, 34, 38, 39, 40, 42, 46, 49, 50, 51, 52, 53, 57, 59, 60, 64, 65, 66, 69, 71, 78, 79, 89, 93, 94, 95, 97, 98, 99},
      'spec': {'column': 'time', 'max_val': datetime.time(11, 24, 55), 'min_val': datetime.time(0, 11, 37), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 3, 5, 10, 11, 12, 18, 19, 21, 22, 23, 25, 26, 27, 30, 31, 32, 35, 36, 37, 41, 43, 44, 45, 47, 48, 54, 55, 56, 61, 62, 67, 70, 72, 73, 74, 77, 80, 81, 82, 83, 84, 85, 86, 88, 90, 92, 96},
      'spec': {'column': 'time', 'max_val': datetime.time(23, 11, 13), 'min_val': datetime.time(13, 40, 27), 'operator': 'IN_RANGE'}
    },
    {
      'expected': set(),
      'spec': {'column': 'datetime', 'operator': 'IN_LIST', 'values': []}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'datetime', 'operator': 'IN_LIST', 'values': [datetime.datetime(2020, 9, 24, 11, 24, 55), datetime.datetime(2011, 12, 9, 13, 40, 27), datetime.datetime(2010, 8, 7, 23, 44, 12), datetime.datetime(2021, 10, 17, 17, 13, 2), datetime.datetime(2013, 7, 4, 10, 48, 5), datetime.datetime(2022, 7, 8, 17, 12), datetime.datetime(2013, 6, 20, 0, 53, 3), datetime.datetime(2019, 12, 17, 12, 19, 43), datetime.datetime(2005, 7, 25, 7, 33, 45), datetime.datetime(2000, 12, 26, 1, 6, 34), datetime.datetime(2003, 2, 23, 14, 41, 46), datetime.datetime(2007, 11, 11, 20, 21, 12), datetime.datetime(2017, 5, 23, 20, 55, 33), datetime.datetime(2022, 10, 24, 12, 36, 15), datetime.datetime(2017, 7, 1, 10, 57, 56), datetime.datetime(2010, 6, 28, 6, 38, 17), datetime.datetime(2009, 7, 23, 6, 58, 34), datetime.datetime(2005, 6, 8, 4, 7, 44), datetime.datetime(2001, 1, 7, 17, 38, 14), datetime.datetime(2005, 5, 27, 17, 35, 48), datetime.datetime(2010, 3, 19, 4, 40, 59), datetime.datetime(2013, 10, 12, 15, 9, 38), datetime.datetime(2007, 10, 9, 21, 23, 29), datetime.datetime(2006, 11, 11, 21, 59, 19), datetime.datetime(2018, 3, 11, 0, 13, 53), datetime.datetime(2016, 12, 14, 17, 30, 14), datetime.datetime(2000, 7, 5, 14, 40, 38), datetime.datetime(2015, 3, 5, 22, 40, 39), datetime.datetime(2004, 8, 31, 3, 13, 27), datetime.datetime(2001, 4, 14, 8, 19, 40), datetime.datetime(2006, 2, 2, 20, 24, 1), datetime.datetime(2021, 10, 2, 22, 20, 4), datetime.datetime(2014, 1, 6, 17, 42, 39), datetime.datetime(2003, 12, 17, 23, 15, 20), datetime.datetime(2019, 7, 26, 3, 20, 46), datetime.datetime(2008, 4, 19, 20, 25, 31), datetime.datetime(2019, 6, 8, 16, 42, 31), datetime.datetime(2010, 10, 2, 22, 15, 59), datetime.datetime(2021, 6, 11, 0, 37, 44), datetime.datetime(2015, 6, 16, 1, 46, 17), datetime.datetime(2005, 4, 1, 0, 24, 1), datetime.datetime(2004, 4, 21, 18, 54, 22), datetime.datetime(2021, 2, 10, 3, 24, 24), datetime.datetime(2019, 9, 28, 22, 17, 8), datetime.datetime(2020, 4, 2, 22, 17, 17), datetime.datetime(2004, 9, 28, 18, 28, 49), datetime.datetime(2008, 4, 22, 9, 15, 21), datetime.datetime(2001, 1, 22, 16, 55, 20), datetime.datetime(2014, 8, 15, 18, 14, 10), datetime.datetime(2016, 1, 18, 0, 11, 37), datetime.datetime(2014, 4, 29, 0, 44, 46), datetime.datetime(2002, 6, 11, 10, 9, 12), datetime.datetime(2015, 10, 28, 10, 43, 15), datetime.datetime(2020, 7, 22, 11, 16, 57), datetime.datetime(2015, 5, 17, 14, 25, 31), datetime.datetime(2019, 3, 23, 14, 6, 35), datetime.datetime(2023, 1, 24, 16, 14, 38), datetime.datetime(2017, 7, 22, 8, 58, 6), datetime.datetime(2021, 4, 21, 23, 15, 27), datetime.datetime(2006, 1, 4, 10, 7, 34), datetime.datetime(2020, 2, 11, 4, 39, 45), datetime.datetime(2018, 12, 1, 20, 3, 52), datetime.datetime(2021, 6, 22, 21, 46, 58), datetime.datetime(2001, 11, 28, 13, 24, 37), datetime.datetime(2015, 4, 5, 1, 56, 52), datetime.datetime(2010, 12, 10, 8, 9, 9), datetime.datetime(2011, 3, 27, 10, 51, 3), datetime.datetime(2012, 10, 13, 19, 19, 52), datetime.datetime(2003, 5, 29, 12, 3, 4), datetime.datetime(2016, 7, 23, 6, 11, 21), datetime.datetime(2004, 5, 23, 16, 1, 11), datetime.datetime(2022, 5, 28, 7, 9, 58), datetime.datetime(2007, 8, 5, 16, 9, 3), datetime.datetime(2007, 10, 3, 14, 7, 44), datetime.datetime(2013, 10, 10, 17, 53, 11), datetime.datetime(2017, 12, 17, 23, 35, 29), datetime.datetime(2010, 12, 24, 11, 29, 53), datetime.datetime(2003, 8, 27, 15, 53, 20), datetime.datetime(2004, 3, 5, 8, 6, 15), datetime.datetime(2016, 8, 27, 9, 23, 28), datetime.datetime(2003, 4, 9, 21, 35, 58), datetime.datetime(2013, 10, 15, 23, 11, 13), datetime.datetime(2005, 7, 26, 20, 21, 17), datetime.datetime(2014, 5, 21, 17, 47, 27), datetime.datetime(2000, 3, 1, 19, 58, 11), datetime.datetime(2018, 3, 10, 22, 28, 52), datetime.datetime(2017, 11, 19, 15, 24, 8), datetime.datetime(2014, 8, 13, 12, 33, 26), datetime.datetime(2006, 7, 11, 14, 29, 36), datetime.datetime(2010, 4, 24, 3, 35, 48), datetime.datetime(2010, 9, 23, 18, 35, 37), datetime.datetime(2022, 4, 1, 11, 52, 44), datetime.datetime(2020, 6, 29, 21, 15, 48), datetime.datetime(2003, 9, 9, 7, 39), datetime.datetime(2008, 1, 4, 4, 34, 48), datetime.datetime(2019, 9, 3, 5, 20, 58), datetime.datetime(2004, 12, 14, 18, 36, 56), datetime.datetime(2016, 5, 26, 0, 16, 33), datetime.datetime(2001, 3, 5, 7, 27, 51), datetime.datetime(2013, 10, 3, 0, 50, 14)]}
    },
    {
      'expected': {8, 11, 15, 16, 17, 19, 20, 22, 23, 28, 30, 35, 40, 45, 46, 59, 70, 72, 73, 82, 88, 89, 94, 96},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2010, 6, 28, 6, 38, 17), 'min_val': datetime.datetime(2004, 5, 23, 16, 1, 11), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 8, 11, 15, 16, 17, 19, 20, 22, 23, 30, 35, 37, 40, 46, 59, 65, 66, 67, 72, 73, 74, 76, 82, 88, 89, 90, 94, 99},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2013, 10, 10, 17, 53, 11), 'min_val': datetime.datetime(2005, 4, 1, 0, 24, 1), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 20, 21, 24, 25, 27, 31, 32, 34, 36, 37, 38, 39, 42, 43, 44, 46, 48, 49, 50, 52, 53, 54, 55, 57, 58, 60, 61, 62, 64, 65, 66, 67, 69, 71, 74, 75, 76, 79, 81, 83, 85, 86, 87, 89, 90, 91, 92, 95, 97, 99},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2022, 10, 24, 12, 36, 15), 'min_val': datetime.datetime(2008, 4, 22, 9, 15, 21), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 11, 12, 14, 15, 16, 20, 21, 22, 25, 27, 32, 35, 37, 39, 46, 48, 49, 50, 52, 54, 57, 64, 65, 66, 67, 69, 73, 74, 75, 76, 79, 81, 83, 85, 86, 87, 89, 90, 94, 97, 99},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2018, 3, 10, 22, 28, 52), 'min_val': datetime.datetime(2007, 10, 3, 14, 7, 44), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 4, 6, 7, 12, 14, 15, 20, 21, 24, 25, 27, 32, 34, 36, 37, 39, 43, 44, 48, 49, 50, 52, 54, 55, 57, 60, 61, 64, 65, 66, 67, 69, 74, 75, 76, 79, 81, 83, 85, 86, 87, 89, 90, 95, 97, 99},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2020, 4, 2, 22, 17, 17), 'min_val': datetime.datetime(2010, 3, 19, 4, 40, 59), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 3, 5, 7, 13, 24, 31, 34, 36, 38, 42, 43, 44, 53, 55, 57, 58, 60, 61, 62, 71, 75, 85, 86, 91, 92, 95},
      'spec': {'column': 'datetime', 'max_val': datetime.datetime(2022, 10, 24, 12, 36, 15), 'min_val': datetime.datetime(2017, 7, 22, 8, 58, 6), 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'name', 'max_val': 'Wilmette', 'min_val': 'Aarika', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {89},
      'spec': {'column': 'name', 'max_val': 'Wilmette', 'min_val': 'Wilmette', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {19},
      'spec': {'column': 'name', 'max_val': 'Aarika', 'min_val': 'Aarika', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 32, 97, 67, 6, 8, 9, 46, 79, 50, 27},
      'spec': {'column': 'name', 'max_val': 'Piper', 'min_val': 'Neysa', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 8, 9, 11, 14, 17, 21, 22, 32, 37, 38, 40, 42, 44, 45, 48, 51, 52, 55, 56, 58, 65, 79, 80, 85, 91, 92, 94, 96, 98},
      'spec': {'column': 'name', 'max_val': 'Noemi', 'min_val': 'Jaynell', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 3, 4, 5, 7, 11, 12, 13, 14, 16, 17, 20, 21, 22, 24, 25, 28, 29, 30, 33, 35, 37, 38, 39, 40, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 77, 80, 82, 83, 85, 86, 87, 88, 90, 92, 94, 95, 96, 99},
      'spec': {'column': 'name', 'max_val': 'Mellisent', 'min_val': 'Abbe', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {2, 99, 68, 5, 47, 87, 25, 30},
      'spec': {'column': 'name', 'max_val': 'Bathsheba', 'min_val': 'Allegra', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {75, 61},
      'spec': {'column': 'name', 'max_val': 'Georgiana', 'min_val': 'Felipa', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {64, 7, 74, 13, 82, 90, 59, 60, 63},
      'spec': {'column': 'name', 'max_val': 'Jaquelin', 'min_val': 'Gustie', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'age', 'max_val': 92, 'min_val': 7, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {4, 5, 7, 10, 16, 20, 22, 23, 25, 29, 34, 35, 38, 40, 41, 42, 44, 45, 49, 52, 53, 54, 57, 62, 64, 65, 66, 68, 69, 70, 71, 73, 78, 81, 83, 84, 85, 86, 87, 88, 89, 92, 93, 96, 99},
      'spec': {'column': 'boolean', 'max_val': False, 'min_val': False, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 24, 26, 27, 28, 30, 31, 32, 33, 36, 37, 39, 43, 46, 47, 48, 50, 51, 55, 56, 58, 59, 60, 61, 63, 67, 72, 74, 75, 76, 77, 79, 80, 82, 90, 91, 94, 95, 97, 98},
      'spec': {'column': 'boolean', 'max_val': True, 'min_val': True, 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 4, 7, 11, 13, 14, 17, 21, 22, 29, 37, 38, 39, 40, 48, 51, 52, 54, 55, 56, 59, 60, 61, 63, 64, 65, 69, 70, 73, 74, 75, 77, 80, 82, 83, 85, 86, 88, 90, 92, 94, 95, 96},
      'spec': {'column': 'name', 'max_val': 'Mellisent', 'min_val': 'Debi', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {34, 67},
      'spec': {'column': 'name', 'max_val': 'Rey', 'min_val': 'Piper', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 4, 6, 7, 8, 9, 11, 13, 14, 17, 21, 22, 32, 37, 38, 39, 40, 42, 44, 45, 46, 48, 51, 52, 54, 55, 56, 58, 59, 60, 61, 63, 64, 65, 69, 70, 73, 74, 75, 77, 79, 80, 82, 83, 85, 86, 88, 90, 91, 92, 94, 96, 98},
      'spec': {'column': 'name', 'max_val': 'Pearla', 'min_val': 'Deena', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {33, 2, 3, 35, 66, 72, 12, 20, 53, 24, 57, 28},
      'spec': {'column': 'name', 'max_val': 'Casi', 'min_val': 'Bathsheba', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {8, 17, 22, 32, 38, 40, 42, 44, 45, 48, 51, 52, 55, 58, 85, 91, 94, 96, 98},
      'spec': {'column': 'name', 'max_val': 'Nicki', 'min_val': 'Karol', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {0, 1, 6, 8, 9, 11, 14, 15, 17, 18, 21, 22, 23, 26, 27, 31, 32, 34, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 48, 50, 51, 52, 55, 58, 65, 67, 76, 78, 79, 80, 81, 84, 85, 91, 92, 93, 94, 96, 97, 98},
      'spec': {'column': 'name', 'max_val': 'Virginia', 'min_val': 'Jeanna', 'operator': 'IN_RANGE'}
    },
    {
      'expected': {1, 2, 3, 4, 7, 11, 12, 13, 14, 20, 21, 24, 25, 28, 29, 30, 33, 35, 37, 39, 49, 52, 53, 54, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72, 73, 74, 75, 77, 80, 82, 83, 86, 87, 88, 90, 92, 95},
      'spec': {'column': 'name', 'max_val': 'Karol', 'min_val': 'Andee', 'operator': 'IN_RANGE'}}
  ],
  'regex_match': [{
      'expected': set(),
      'spec': {'column': 'name', 'expression': '', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99},
      'spec': {'column': 'name', 'expression': '.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'a.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'b.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'c.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'd.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'e.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'f.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'g.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'h.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'i.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'j.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'k.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'l.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'm.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'n.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'o.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'p.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'q.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'r.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 's.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 't.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'u.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'v.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'w.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'x.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'y.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'z.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {99, 68, 5, 47, 16, 19, 87, 25, 30},
      'spec': {'column': 'name', 'expression': 'A.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {33, 2, 35, 66, 72, 53, 57, 28},
      'spec': {'column': 'name', 'expression': 'B.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {3, 71, 12, 49, 20, 24, 62},
      'spec': {'column': 'name', 'expression': 'C.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {70, 54, 86, 29, 95},
      'spec': {'column': 'name', 'expression': 'D.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {83, 77, 69, 39},
      'spec': {'column': 'name', 'expression': 'E.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {61},
      'spec': {'column': 'name', 'expression': 'F.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {4, 73, 75, 88, 59},
      'spec': {'column': 'name', 'expression': 'G.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'H.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {64, 13, 82, 90, 60},
      'spec': {'column': 'name', 'expression': 'I.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {65, 37, 7, 74, 11, 14, 80, 21, 56, 63},
      'spec': {'column': 'name', 'expression': 'J.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {1, 52, 92, 55},
      'spec': {'column': 'name', 'expression': 'K.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {48, 17, 38, 94},
      'spec': {'column': 'name', 'expression': 'L.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {96, 98, 40, 45, 51, 85, 22, 58, 91},
      'spec': {'column': 'name', 'expression': 'M.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {32, 6, 8, 9, 42, 44, 79},
      'spec': {'column': 'name', 'expression': 'N.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {46},
      'spec': {'column': 'name', 'expression': 'O.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {0, 97, 67, 50, 27},
      'spec': {'column': 'name', 'expression': 'P.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'Q.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {34, 36, 76, 78, 81, 26},
      'spec': {'column': 'name', 'expression': 'R.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {18, 23},
      'spec': {'column': 'name', 'expression': 'S.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {93, 31, 84, 15},
      'spec': {'column': 'name', 'expression': 'T.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'U.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {41, 10, 43},
      'spec': {'column': 'name', 'expression': 'V.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {89},
      'spec': {'column': 'name', 'expression': 'W.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'X.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'Y.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': 'Z.*', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {0, 2, 5, 12, 19, 20, 26, 27, 31, 32, 36, 37, 38, 42, 43, 46, 47, 49, 50, 55, 60, 61, 64, 66, 68, 69, 70, 73, 75, 81, 88, 99},
      'spec': {'column': 'name', 'expression': '.*a', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*b', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*c', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {58, 82, 45},
      'spec': {'column': 'name', 'expression': '.*d', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {7, 10, 11, 14, 15, 16, 21, 28, 30, 39, 40, 41, 44, 48, 57, 59, 65, 79, 83, 87, 89, 95, 98},
      'spec': {'column': 'name', 'expression': '.*e', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*f', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {85},
      'spec': {'column': 'name', 'expression': '.*g', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {18, 6},
      'spec': {'column': 'name', 'expression': '.*h', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {3, 4, 35, 8, 9, 84, 23, 24, 92, 29},
      'spec': {'column': 'name', 'expression': '.*i', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*j', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*k', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {56, 97, 52},
      'spec': {'column': 'name', 'expression': '.*l', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*m', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {1, 71, 74, 77, 80, 86, 90, 62, 63},
      'spec': {'column': 'name', 'expression': '.*n', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*o', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*p', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*q', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {67},
      'spec': {'column': 'name', 'expression': '.*r', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {54},
      'spec': {'column': 'name', 'expression': '.*s', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {96, 51, 53, 78},
      'spec': {'column': 'name', 'expression': '.*t', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*u', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*v', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*w', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*x', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': {33, 34, 72, 76, 13, 17, 22, 25, 91, 93, 94},
      'spec': {'column': 'name', 'expression': '.*y', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*z', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*A', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*B', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*C', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*D', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*E', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*F', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*G', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*H', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*I', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*J', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*K', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*L', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*M', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*N', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*O', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*P', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*Q', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*R', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*S', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*T', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*U', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*V', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*W', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*X', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*Y', 'operator': 'REGEX_MATCH'}
    },
    {
      'expected': set(),
      'spec': {'column': 'name', 'expression': '.*Z', 'operator': 'REGEX_MATCH'}
    }
  ]
}
