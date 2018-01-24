import pymysql
import time
from _datetime import datetime


# 打开数据库连接
db = pymysql.connect("localhost","goaler","123456","harmony")

# 创建游标
cursor = db.cursor()

# 使用游标cursor执行sql
cursor.execute("select version()")

# 获取单条数据
data = cursor.fetchone()

print("Database version :%s" % data)

# 获取多条数据
cursor.execute("select * from user")
results = cursor.fetchall()
for r in results:
    print(r)


# 插入数据
sql = "insert into user(usercode,nickname,email,password,type,state,create_time)\
    values('%s','%s','%s','%s','%d','%d','%s')" % \
    ("goaler","goaler",'goaler@nineteens.com','123456',1,1,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

try:
    print(sql)
    cursor.execute(sql)
    print("success")
    db.commit()
except Exception as e:
    db.rollback()
    print("fail")
    print(e)




# 关闭数据库连接
db.close()




input("Press <enter> exit!")
exit()
