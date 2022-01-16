import requests
import re
import datetime
import json
import MySQLdb as mdb
import time
from urllib import request as urlrequest
from fp.fp import FreeProxy
from fake_useragent import UserAgent
import socket


new_list = []
domain_list = []
updated_domain_list = []
s = requests.Session()


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
        

#selecting new updated domain names
sql4 = ' SELECT domain_name FROM domain_tool WHERE govalue IS NULL OR govalue = " "'
cur.execute(sql4)
myresult1 = cur.fetchall()
myresult1 = list(myresult1)
for lines in myresult1:
    lines =  ''.join(lines)
    
    updated_domain_list.append(lines)
print('updated')

def get_proxy():
    proxy = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()
    proxy = proxy[7:]
    print(proxy)
    url = 'http://icanhazip.com'
    request = urlrequest.Request(url)
    request.set_proxy(proxy, 'http')
    response = urlrequest.urlopen(request)
    


#updating the govalue
def get_function(line):
    r = s.get('https://api.godaddy.com/v1/appraisal/'+line)
    get_function.json_data = json.loads(r.text)
    govalue = get_function.json_data['govalue']
    print(govalue)
    sql = "UPDATE domain_tool SET govalue = %s  WHERE domain_name = %s"
    val = (govalue, line)
    cur.execute(sql, val)
    db.commit()

for lines in updated_domain_list:
        try:
                get_function(lines)
        except:
                print("fa")
                time.sleep(0.5)
                if(get_function.json_data['status'] == 'SLOW_DOWN'):
                        new_list.append(lines)
                        get_proxy()
                        hostname = socket.gethostname()
                        local_ip = socket.gethostbyname(hostname)
                        print(local_ip)
                        ua = UserAgent()
                        ua.chrome

#updating govalue from new_list
def get_new(line):
        r = s.get('https://api.godaddy.com/v1/appraisal/'+line)
        json_data = json.loads(r.text)
        govalue = json_data['govalue']
        sql = "UPDATE domain_tool SET govalue = %s  WHERE domain_name = %s"
        val = (govalue, line)
        cur.execute(sql, val)
        db.commit()


for lines in new_list:
        try:
                get_new(lines)
                print(lines)
                print(new_list)
        except:
                print(lines)
                time.sleep(10)
                new_list.append(lines)
                print(new_list)

db.close()
