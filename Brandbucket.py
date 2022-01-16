from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests
from urllib.request import Request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}




my_url_2 ='https://www.brandbucket.com/names'
s = requests.Session()
response = s.get(my_url_2, headers=headers)
print(response.text)
#uClient = uReq(my_url_2)
req = Request(
    my_url_2, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
)
uClient = uReq(req)
page_html = uClient.read()

page_soup = soup(page_html,"html.parser")
Html_file= open("new3.html","w", encoding="utf-8")

containers = page_soup.findAll('div',{'class': "domainCardDetail"})
length = len(containers)
print(soup.prettify(containers[0]))
i = 0
while i < length:
    container= str(containers[i])
##    print(container)
    pattern = "<span>(.*?)</span>"
    i = i+ 1
    substring = re.findall(pattern, container)
    print(substring)
    


Html_file.write(response.text)
Html_file.close()

##final = containers.findAll('div',{'class': "results marginbottom40"})
##print(final)

##final2 = final.find('div',{'class': "results marginbottom40"})
##print(final2)


