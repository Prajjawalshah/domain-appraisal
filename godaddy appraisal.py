import requests
s = requests.Session()
file1 = open('dynadomains', 'r') 
Lines = file1.readlines() 
#r = s.get('https://api.godaddy.com/v1/appraisal/thehackernews.com', cookies={'xpdpp3': 'B','currency':'INR'})
#print(r.text)
# '{"cookies": {"from-my": "browser"}}'
for lines in Lines:
        r = s.get('https://api.godaddy.com/v1/appraisal/'+lines)
        print(r.text)
# '{"cookies": {}}'
