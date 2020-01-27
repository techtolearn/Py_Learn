# https://www.youtube.com/watch?v=ng2o98k983k&index=46&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
Python Tutorial: Web Scraping with BeautifulSoup and Requests
'''

from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')  # lxml will gather all html tags

#print(soup.prettify())

'''
the below exampleis writtend for grabbing only one articale
'''
# parsing information
'''
article= soup.find('article')
#print(article.prettify())

#headline = article.h2.a.text
#print(headline)
#summary = article.find('div',class_='entry-content').p.text   # p means paragraph
#print(summary)


vid_src= article.find('iframe', class_='youtube-player')['src']
print(vid_src)
print('\n')
vid_id = vid_src.split('/')  #get the 4 index
print(vid_id)
print('\n')
vid_id = vid_src.split('/')[4]
print(vid_id)
print('\n')
#vid_id = vid_id.split('?')
#print(vid_id)
print('\n')
video_id = vid_id.split('?')[0]
print(video_id)

# you can create your own formate youtub linke using this id

yt_link = f'https://youtube.com/watch?v={video_id}'
print(yt_link)
'''
'''
you can simple grab all the articale of the given website and related video using same code with little modificaiton
'''

#**********************************************************************************************************************

csv_file = open('cms.WebScraping.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','VideoLink'])

for article in  soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div',class_='entry-content').p.text   # p means paragraph
    print(summary)
    # if any video is missing from the website content, try catch exception will set that video as None else print the video link
    try:
        vid_src= article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        video_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = 'None'

    print(yt_link)
    print('\n')
    csv_writer.writerow([headline,summary,yt_link])
csv_file.close
