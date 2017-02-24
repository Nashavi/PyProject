import bs4 as bs
import urllib2
import time
import random

# artist = 'u/u2'
# firstothertitle = "11 O'Clock Tick Tock"

artist = 'c/coldplay'
firstothertitle = "1.36"
filename = "coldplay.csv"


artisturl = 'http://www.azlyrics.com/' + artist +'.html'

artisthome = urllib2.urlopen(artisturl)

soup = bs.BeautifulSoup(artisthome,'html.parser')

titlelists= soup.body.find(id = "listAlbum")

albums = soup.body.find_all('div', class_='album')

titles = titlelists.find_all('a')

f = open(filename, "w")

f.write("title, album, link, lyrics\n")

c = 0
for title in titles[1:]:
    if (title.text) == firstothertitle:
        c = c + 1
        print " "
    if (title.text.strip()) != '':

        titleurl = title['href'].replace("..","http://www.azlyrics.com")

        time.sleep(random.choice([7, 10, 12, 16, 18, 20]))

        titlehome = urllib2.urlopen(titleurl)

        titleurlsoup = bs.BeautifulSoup(titlehome, 'html.parser')

        for div in titleurlsoup.body.find_all('div', class_=''):
            lyrics = div.text.strip().replace(",", "|")

        print (title.text.replace(",", ".")) + ", " + (albums[c].text) + ", " + (title['href'].replace("..", "http://www.azlyrics.com")) + ", " + lyrics

        f.write(title.text.replace(",", ".") + ", " + (albums[c].text) + ", " + (title['href'].replace("..", "http://www.azlyrics.com")) + ", " + lyrics + "/n")

    else:
        print " "
        c = c + 1

f.close()