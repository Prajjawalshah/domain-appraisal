import requests
import re
import datetime
import json
import MySQLdb as mdb
import time

s = requests.Session()
domain_list = []

#dbms login and connection
DBNAME = yourdbname
DBHOST = yourhost
DBPASS = yourpassword
DBUSER = youruser
db = mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
print("Database Connected Successfully")
cur = db.cursor()
now = datetime.datetime.now()

#delete duplicates
sql3 = 'DELETE t1 FROM domain_tool t1, domain_tool t2 WHERE t1.id < t2.id AND t1.domain_name = t2.domain_name'
cur.execute(sql3)

#selecting domain names
sql = ' SELECT domain_name FROM domain_tool'
cur.execute(sql)
myresult = cur.fetchall()
myresult = list(myresult)
for lines in myresult:
    lines =  ''.join(lines)
    
    domain_list.append(lines)

#deleting the expired
for lines in domain_list:
        sql = 'SELECT expiring_date FROM domain_tool WHERE domain_name = %s'
#        val = nd.array2string(lines)[2:-2]
        val = lines
        
        cur.execute(sql,[val])
        myresult = cur.fetchall()
        myfinal = '\n'.join([k for k, in myresult])[:-7]
        then= datetime.datetime.strptime(myfinal,'%Y-%m-%d %H:%M:%S')
        num = then - now
        if num <= datetime.timedelta(0):
           print("deleted")
           sql2 = 'DELETE FROM domain_tool WHERE domain_name = %s'
           cur.execute(sql2,[val])
           db.commit()
        else:
            break



db.close()
