#coding=utf-8

import MySQLdb

print 'hello!'


db = MySQLdb.connect("192.168.0.106","dataview",'''view2{:>}"?3''',"chaos_formal")
db2 = MySQLdb.connect("localhost","yy",'''123456''',"test")

cur = db.cursor()
cur2 = db2.cursor()

cur.execute('''
SELECT
    mobile,
    COUNT(*)
FROM
    TMP_MEMBER_TRACK
WHERE
    verification_type = 'SECOND_NO_AUTH'
AND mobile is not NULL
AND access_time BETWEEN '2018-01-15'
AND '2018-01-22'
GROUP BY
    mobile
''')
res = cur.fetchall()

i = 1;
for r in res:
    if i == 1:
        i+=1
        continue
    print "第%d条/总共%d条" % (i,len(res))
    i+=1
    print r
    cur.execute('''
    SELECT
        store_id,
        mobile,
        type_defined_id,
        verification_type,
        access_time
    FROM
        TMP_MEMBER_TRACK
    WHERE
        mobile = '%s'
    AND access_time < '2018-01-15'
    AND verification_type <> 'SECOND_NO_AUTH'
    AND LENGTH(mobile) > 0
    ORDER BY
        access_time DESC
    LIMIT 1
    ''' % r[0])
    data = cur.fetchone()
    
    print data
    if data is not None and len(data) == 5:
        sql = '''
        INSERT INTO `data` (
            `store_id`,
            `mobile`,
            `type_defined_id`,
            `verification_type`,
            `access_time`
        )
        VALUES
            ('%s', '%s', '%s', '%s', '%s');
        ''' % (data[0],data[1],data[2],data[3],data[4])
        print sql
        cur2.execute(sql)
        db2.commit()
             




























print "end"
# raw_input("Press <enter> exit!")
# exit()
