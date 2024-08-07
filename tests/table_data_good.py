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
names = ['Pearla', 'Karleen', 'Bathsheba', 'Casi', 'Gusti', 'Anastassia', 'Nonah', 'Janine', 'Nicki', 'Noemi', 'Vivyanne', 'Jeanne', 'Carina', 'Ivy', 'Jenine', 'Tandie', 'Abbe', 'Laney', 'Shandeigh', 'Aarika', 'Caria', 'Jorrie', 'Maisey', 'Shani', 'Casi', 'Ashley', 'Roselia', 'Petronia', 'Brandice', 'Debi', 'Andee', 'Teodora', 'Neysa', 'Beverley', 'Rey', 'Brittni', 'Rheba', 'Jeanna', 'Lyssa', 'Elayne', 'Magdalene', 'Violante', 'Netta', 'Virginia', 'Natalie', 'Mildred', 'Ophelia', 'Alma', 'Lettie', 'Catherina', 'Philipa', 'Marget', 'Karol', 'Berget', 'Doloritas', 'Kessia', 'Jaynell', 'Bethanne', 'Mildred', 'Gustie', 'Irina', 'Felipa', 'Charlean', 'Jaquelin', 'Isadora', 'Jelene', 'Benedicta', 'Piper', 'Almeria', 'Editha', 'Deena', 'Celestyn', 'Betsy', 'Georgianna', 'Jacklin', 'Georgiana', 'Robby', 'Emmalyn', 'Robinett', 'Nickie', 'Jo-Ann', 'Rosita', 'Ingrid', 'Erminie', 'Tami', 'Meg', 'Devan', 'Annaliese', 'Ginevra', 'Wilmette', 'Imogen', 'Melony', 'Kalli', 'Tessy', 'Lesly', 'Deedee', 'Mellisent', 'Perl', 'Milzie', 'Allegra']
ages = [64, 78, 79, 13, 28, 70, 79, 87, 31, 7, 46, 51, 29, 13, 43, 17, 83, 29, 46, 55, 60, 37, 50, 9, 57, 88, 74, 47, 67, 42, 82, 63, 79, 81, 34, 77, 80, 51, 68, 61, 72, 71, 59, 55, 31, 57, 31, 66, 91, 45, 58, 59, 77, 15, 42, 39, 92, 82, 90, 77, 60, 20, 23, 31, 83, 34, 89, 83, 55, 38, 45, 51, 10, 90, 55, 85, 38, 53, 75, 11, 74, 80, 52, 31, 69, 25, 76, 63, 11, 77, 33, 18, 19, 53, 64, 11, 17, 50, 92, 55]
date_strings = ['2020-09-24', '2011-12-09', '2010-08-07', '2021-10-17', '2013-07-04', '2022-07-08', '2013-06-20', '2019-12-17', '2005-07-25', '2000-12-26', '2003-02-23', '2007-11-11', '2017-05-23', '2022-10-24', '2017-07-01', '2010-06-28', '2009-07-23', '2005-06-08', '2001-01-07', '2005-05-27', '2010-03-19', '2013-10-12', '2007-10-09', '2006-11-11', '2018-03-11', '2016-12-14', '2000-07-05', '2015-03-05', '2004-08-31', '2001-04-14', '2006-02-02', '2021-10-02', '2014-01-06', '2003-12-17', '2019-07-26', '2008-04-19', '2019-06-08', '2010-10-02', '2021-06-11', '2015-06-16', '2005-04-01', '2004-04-21', '2021-02-10', '2019-09-28', '2020-04-02', '2004-09-28', '2008-04-22', '2001-01-22', '2014-08-15', '2016-01-18', '2014-04-29', '2002-06-11', '2015-10-28', '2020-07-22', '2015-05-17', '2019-03-23', '2023-01-24', '2017-07-22', '2021-04-21', '2006-01-04', '2020-02-11', '2018-12-01', '2021-06-22', '2001-11-28', '2015-04-05', '2010-12-10', '2011-03-27', '2012-10-13', '2003-05-29', '2016-07-23', '2004-05-23', '2022-05-28', '2007-08-05', '2007-10-03', '2013-10-10', '2017-12-17', '2010-12-24', '2003-08-27', '2004-03-05', '2016-08-27', '2003-04-09', '2013-10-15', '2005-07-26', '2014-05-21', '2000-03-01', '2018-03-10', '2017-11-19', '2014-08-13', '2006-07-11', '2010-04-24', '2010-09-23', '2022-04-01', '2020-06-29', '2003-09-09', '2008-01-04', '2019-09-03', '2004-12-14', '2016-05-26', '2001-03-05', '2013-10-03']
dates = [datetime.date.fromisoformat(date_string) for date_string in date_strings]
time_strings = ['11:24:55', '13:40:27', '23:44:12', '17:13:02', '10:48:05', '17:12:00', '00:53:03', '12:19:43', '07:33:45', '01:06:34', '14:41:46', '20:21:12', '20:55:33', '12:36:15', '10:57:56', '06:38:17', '06:58:34', '04:07:44', '17:38:14', '17:35:48', '04:40:59', '15:09:38', '21:23:29', '21:59:19', '00:13:53', '17:30:14', '14:40:38', '22:40:39', '03:13:27', '08:19:40', '20:24:01', '22:20:04', '17:42:39', '23:15:20', '03:20:46', '20:25:31', '16:42:31', '22:15:59', '00:37:44', '01:46:17', '00:24:01', '18:54:22', '03:24:24', '22:17:08', '22:17:17', '18:28:49', '09:15:21', '16:55:20', '18:14:10', '00:11:37', '00:44:46', '10:09:12', '10:43:15', '11:16:57', '14:25:31', '14:06:35', '16:14:38', '08:58:06', '23:15:27', '10:07:34', '04:39:45', '20:03:52', '21:46:58', '13:24:37', '01:56:52', '08:09:09', '10:51:03', '19:19:52', '12:03:04', '06:11:21', '16:01:11', '07:09:58', '16:09:03', '14:07:44', '17:53:11', '23:35:29', '11:29:53', '15:53:20', '08:06:15', '09:23:28', '21:35:58', '23:11:13', '20:21:17', '17:47:27', '19:58:11', '22:28:52', '15:24:08', '12:33:26', '14:29:36', '03:35:48', '18:35:37', '11:52:44', '21:15:48', '07:39:00', '04:34:48', '05:20:58', '18:36:56', '00:16:33', '07:27:51', '00:50:14']
times = [datetime.time.fromisoformat(time_string) for time_string in time_strings]
datetime_strings =['2020-09-24T11:24:55', '2011-12-09T13:40:27', '2010-08-07T23:44:12', '2021-10-17T17:13:02', '2013-07-04T10:48:05', '2022-07-08T17:12:00', '2013-06-20T00:53:03', '2019-12-17T12:19:43', '2005-07-25T07:33:45', '2000-12-26T01:06:34', '2003-02-23T14:41:46', '2007-11-11T20:21:12', '2017-05-23T20:55:33', '2022-10-24T12:36:15', '2017-07-01T10:57:56', '2010-06-28T06:38:17', '2009-07-23T06:58:34', '2005-06-08T04:07:44', '2001-01-07T17:38:14', '2005-05-27T17:35:48', '2010-03-19T04:40:59', '2013-10-12T15:09:38', '2007-10-09T21:23:29', '2006-11-11T21:59:19', '2018-03-11T00:13:53', '2016-12-14T17:30:14', '2000-07-05T14:40:38', '2015-03-05T22:40:39', '2004-08-31T03:13:27', '2001-04-14T08:19:40', '2006-02-02T20:24:01', '2021-10-02T22:20:04', '2014-01-06T17:42:39', '2003-12-17T23:15:20', '2019-07-26T03:20:46', '2008-04-19T20:25:31', '2019-06-08T16:42:31', '2010-10-02T22:15:59', '2021-06-11T00:37:44', '2015-06-16T01:46:17', '2005-04-01T00:24:01', '2004-04-21T18:54:22', '2021-02-10T03:24:24', '2019-09-28T22:17:08', '2020-04-02T22:17:17', '2004-09-28T18:28:49', '2008-04-22T09:15:21', '2001-01-22T16:55:20', '2014-08-15T18:14:10', '2016-01-18T00:11:37', '2014-04-29T00:44:46', '2002-06-11T10:09:12', '2015-10-28T10:43:15', '2020-07-22T11:16:57', '2015-05-17T14:25:31', '2019-03-23T14:06:35', '2023-01-24T16:14:38', '2017-07-22T08:58:06', '2021-04-21T23:15:27', '2006-01-04T10:07:34', '2020-02-11T04:39:45', '2018-12-01T20:03:52', '2021-06-22T21:46:58', '2001-11-28T13:24:37', '2015-04-05T01:56:52', '2010-12-10T08:09:09', '2011-03-27T10:51:03', '2012-10-13T19:19:52', '2003-05-29T12:03:04', '2016-07-23T06:11:21', '2004-05-23T16:01:11', '2022-05-28T07:09:58', '2007-08-05T16:09:03', '2007-10-03T14:07:44', '2013-10-10T17:53:11', '2017-12-17T23:35:29', '2010-12-24T11:29:53', '2003-08-27T15:53:20', '2004-03-05T08:06:15', '2016-08-27T09:23:28', '2003-04-09T21:35:58', '2013-10-15T23:11:13', '2005-07-26T20:21:17', '2014-05-21T17:47:27', '2000-03-01T19:58:11', '2018-03-10T22:28:52', '2017-11-19T15:24:08', '2014-08-13T12:33:26', '2006-07-11T14:29:36', '2010-04-24T03:35:48', '2010-09-23T18:35:37', '2022-04-01T11:52:44', '2020-06-29T21:15:48', '2003-09-09T07:39:00', '2008-01-04T04:34:48', '2019-09-03T05:20:58', '2004-12-14T18:36:56', '2016-05-26T00:16:33', '2001-03-05T07:27:51', '2013-10-03T00:50:14']
datetimes = [datetime.datetime.fromisoformat(datetime_string) for datetime_string in datetime_strings]
booleans = [True, True, True, True, False, False, True, False, True, True, False, True, True, True, True, True, False, True, True, True, False, True, False, False, True, False, True, True, True, False, True, True, True, True, False, False, True, True, False, True, False, False, False, True, False, False, True, True, True, False, True, True, False, False, False, True, True, False, True, True, True, True, False, True, False, False, False, True, False, False, False, False, True, False, True, True, True, True, False, True, True, False, True, False, False, False, False, False, False, False, True, True, False, False, True, True, False, True, True, False]


series_for_name = {'name': names, 'age': ages, 'date': dates, 'time': times,
                   'datetime': datetimes, 'boolean': booleans}
        

    

