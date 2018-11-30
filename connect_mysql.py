#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Lenovo
# Time:2018/11/30 16:43
import MySQLdb
mdb = MySQLdb.connect("***","root","***,"python",charset='utf8')
cursor = mdb.cursor()
sql = """INSERT INTO SIASPEDRO(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    mdb.commit()
except:
    mdb.rollback()
mdb.close()
print("OK！")