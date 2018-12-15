#-*- coding:utf-8 -*-
#!/usr/bin/python3
import time
import pymysql
import Mmongoo 
# 打开数据库连接
db = pymysql.connect("127.0.0.1","root","j24b2qc8qa@#","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("show variables")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
mgo = Mmongoo.Mongoo('mysqldatas')
table = mgo.getApp()
datas = [] 
while(True):
    time.sleep(1)
    dicts = {}
    for ii in data:
        dicts[ii[0]] = ii[1]
    table.insert(dicts)
#table.insert_many(datas)
 
# 关闭数据库连接
db.close()
