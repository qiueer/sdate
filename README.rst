simple datetime
===============

A library that we can get datetime simply and easily

Installation
------------

Install using pip::

    pip install sdate
    
Install using source code::

	git clone https://github.com/qiueer/sdate
	cd sdate
	python setup.py install


Usage
-----

Get datetime information currently::

    >>> from sdate import sdate
    >>> sdate()
    {   'date': '2016-03-14',
	    'datetime': '2016-03-14 11:42:21',
	    'datetimestr': '20160314114221284',
	    'day': 14,
	    'hour': 11,
	    'iso8601': '2016-03-14T11:42:21',
	    'iso8601_ms': '2016-03-14T11:42:21.284319+08:00',
	    'iso8601_ms_tz': '2016-03-14T11:42:21.284319+08:00',
	    'iso8601_tz': '2016-03-14T11:42:21+08:00',
	    'microsecond': 284319,
	    'minute': 42,
	    'month': 3,
	    'second': 21,
	    'tzname': 'GMT+8',
	    'unix_timestamp': 1457926941,
	    'weekday': 0,
	    'year': 2016}
	    
Get datetime information, before four hours::
	>>> from sdate import sdate
	>>> sdate(hours=-4)
	{   'date': '2016-03-14',
	    'datetime': '2016-03-14 07:51:12',
	    'datetimestr': '20160314075112200',
	    'day': 14,
	    'hour': 7,
	    'iso8601': '2016-03-14T07:51:12',
	    'iso8601_ms': '2016-03-14T07:51:12.200265+08:00',
	    'iso8601_ms_tz': '2016-03-14T07:51:12.200265+08:00',
	    'iso8601_tz': '2016-03-14T07:51:12+08:00',
	    'microsecond': 200265,
	    'minute': 51,
	    'month': 3,
	    'second': 12,
	    'tzname': 'GMT+8',
	    'unix_timestamp': 1457913072,
	    'weekday': 0,
	    'year': 2016}
	    
Convert unix timestamp to sdate, that we can use it to get more information::

	>>> from sdate import sdate
	>>>sd=sdate().from_unix_timestamp(1457895842)
	>>>print sd
	{   'date': '2016-03-14',
	    'datetime': '2016-03-14 03:04:02',
	    'datetimestr': '201603140304020',
	    'day': 14,
	    'hour': 3,
	    'iso8601': '2016-03-14T03:04:02',
	    'iso8601_ms': '2016-03-14T03:04:02+08:00',
	    'iso8601_ms_tz': '2016-03-14T03:04:02+08:00',
	    'iso8601_tz': '2016-03-14T03:04:02+08:00',
	    'microsecond': 0,
	    'minute': 4,
	    'month': 3,
	    'second': 2,
	    'tzname': 'GMT+8',
	    'unix_timestamp': 1457895842,
	    'weekday': 0,
	    'year': 2016}
	>>> sd.datetime_str()
	'201603140304020'
	
Reset sdate, the arguments are same as Constructor::

	>>>sd=sdate().from_unix_timestamp(1457895842)
	>>>print sd
	{   'date': '2016-03-14',
	    'datetime': '2016-03-14 03:04:02',
	    'datetimestr': '201603140304020',
	    'day': 14,
	    'hour': 3,
	    'iso8601': '2016-03-14T03:04:02',
	    'iso8601_ms': '2016-03-14T03:04:02+08:00',
	    'iso8601_ms_tz': '2016-03-14T03:04:02+08:00',
	    'iso8601_tz': '2016-03-14T03:04:02+08:00',
	    'microsecond': 0,
	    'minute': 4,
	    'month': 3,
	    'second': 2,
	    'tzname': 'GMT+8',
	    'unix_timestamp': 1457895842,
	    'weekday': 0,
	    'year': 2016}
	>>> sd.reset()
	{   'date': '2016-03-14',
	    'datetime': '2016-03-14 13:05:13',
	    'datetimestr': '20160314130513729',
	    'day': 14,
	    'hour': 13,
	    'iso8601': '2016-03-14T13:05:13',
	    'iso8601_ms': '2016-03-14T13:05:13.729126+08:00',
	    'iso8601_ms_tz': '2016-03-14T13:05:13.729126+08:00',
	    'iso8601_tz': '2016-03-14T13:05:13+08:00',
	    'microsecond': 729126,
	    'minute': 5,
	    'month': 3,
	    'second': 13,
	    'tzname': 'GMT+8',
	    'unix_timestamp': 1457931913,
	    'weekday': 0,
	    'year': 2016}

Support + Contributing
----------------------

Feel free to make pull requests, or report issues via the repo:

https://github.com/qiueer/sdate