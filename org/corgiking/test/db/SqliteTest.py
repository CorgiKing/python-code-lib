import sqlite3


conn = sqlite3.connect("testdb")

print("sqlite test db connect success !")

cur = conn.cursor()

# 新建数据库
createTableSql = '''create table user
       (id            int     not null primary key,
       name           text    not null,
       age            int     not null,
       address        char(50),
       salary         float);'''
cur.execute(createTableSql)
print("Table created successfully")


# 插入数据
insertSql = ''' insert into user values
    (1, 'corgiking', 25, '天之涯', 1000),
    (2, 'goaler', 25, '海之角', 1000)                
                    '''
cur.execute(insertSql)
conn.commit()





