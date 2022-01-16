from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}




#my_url = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
my_url_2 ='https://www.brandbucket.com/names'
s = requests.Session()
response = s.get(my_url_2, headers=headers)
print(response.text)
uClient = uReq(my_url_2)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.find('div',{'class': "_4rR01T"})
print(containers)

Html_file= open("new3.html","w", encoding="utf-8")
Html_file.write(response.text)
Html_file.close()

##final = containers.findAll('div',{'class': "results marginbottom40"})
##print(final)

##final2 = final.find('div',{'class': "results marginbottom40"})
##print(final2)


