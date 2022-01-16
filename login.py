from requests import Session
from bs4 import BeautifulSoup as bs
import requests

 
with requests.Session() as s:
    site = s.get("https://www.name.com/account/login")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"csrf_token"})["value"]
    print(token)
    login_data = {"acct_name":"prajjawal","password":"9425377887@Shah", "csrf_token":token}
    r1= s.post("https://www.name.com/account/login",login_data)
    print(r1.content)
    
    url = "https://www.name.com/api/expired/get_expired_domains_csv"
    r2 = s.get(url, cookies=r1.cookies)
    open('folder.csv', 'wb').write(r2.content)
    print(r2.content)


