#coding:utf8
import MySQLdb
try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123',db='test',charset='utf8') #建立数据库连接
    cursor = conn.cursor() # 建立数据库操作游标
except Exception,e:
    print str(e)
    exit()

#增删改
# sql = 'insert into stu(name) values("%s")' % '洞洞'
#
# try:
#     res = cursor.execute(sql)
#     if res != 0:
#         conn.commit()
# except Exception,e:
#     print str(e)

#查询
sql = 'select * from stu'
cursor.execute(sql)
rows = cursor.fetchall() # 获取查询结果集
print rows

conn.close()