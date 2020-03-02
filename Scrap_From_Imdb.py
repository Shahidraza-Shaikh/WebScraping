#Created By Shahid Shaikh

import requests
from  requests_html import HTMLSession
import csv
# print(r.text) 
session = HTMLSession()
req=session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
Title=req.html.find('.titleColumn')
rating=req.html.find('.imdbRating')

img=req.html.find('.posterColumn a img')

header=['Title','Rating','Images']
data =open('file.csv','w')
writer1=csv.writer(data)
writer1.writerow(header)

for i in range(len(Title)):
    li=[Title[i].text,rating[i].text,img[i].attrs['src']]
    writer1.writerow(li) 