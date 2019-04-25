# -*- coding:utf-8 -*-
import datetime
from mysql_demo import Mysql_demo
a = Mysql_demo()
sql = 'select drop_type from book GROUP BY drop_type;'
m = a.search(sql)
x = list()
for i in range(len(m)):
    x.append(m[i][0])
x = tuple(x)
print(x)