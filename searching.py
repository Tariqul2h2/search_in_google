from urllib import request
from bs4 import BeautifulSoup
from googlesearch import search

#the url you wanted to get data
url = "http://www.ugc-universities.gov.bd/private-universities"

soup = BeautifulSoup(request.urlopen(url).read())
SAVE_SEARCH = []
#my required data in span 
for span in soup.findAll('table')[0].findAll('span'):
    #converting tag into string
    SAVE_SEARCH.append(str(span))
UNIVERSITY_LIST = []
for i in SAVE_SEARCH:
    if 'www.' not in i:
        UNIVERSITY_LIST.append(i.split('>')[1])

for i in UNIVERSITY_LIST:
    m = i.split('<')[0]
    for query in search(f'{m} career',num=2):
        print(query)