# sdate
=========================================

##  功能说明
```
帮助开发者简易、方便地获取时间信息
```

## 安装方法
```
1）源码安装：
git clone https://github.com/qiueer/sdate
cd sdate
python setup.py install
2）pip安装
pip install sdate
```

## 使用示例
获取当前时间信息：
```
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
```

获取四个小时前的时间信息：
```
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
```

将时间戳转化为sdate对象，并获取对应的时间信息：
```
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
```

重置，重置函数的参数跟sdate的构造函数一样：
```
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
```


## 技术交流
```
GITHUB: https://github.com/qiueer/sdate
QQ: 86877295
```