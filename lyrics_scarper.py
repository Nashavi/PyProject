import bs4 as bs
import urllib2
import time
import random
import re

artist = 'u/u2'
firstothertitle = "11 O'Clock Tick Tock"

# artist = 'c/coldplay'
# firstothertitle = "1.36"
filename = "u2.csv"

artisturl = 'http://www.azlyrics.com/' + artist + '.html'

artisthome = urllib2.urlopen(artisturl)

soup = bs.BeautifulSoup(artisthome, 'html.parser')

titlelists = soup.body.find(id="listAlbum")

albums = soup.body.find_all('div', class_='album')

titles = titlelists.find_all('a')

f = open(filename, "w")

f.write("title, release, album, year, link, lyrics\n")

c = 0
for title in titles[1:]:
    if (title.text) == firstothertitle:
        c = c + 1
        print " "
    if (title.text.strip()) != '':

        titleurl = title['href'].replace("..", "http://www.azlyrics.com")

        titlehome = urllib2.urlopen(titleurl)

        titleurlsoup = bs.BeautifulSoup(titlehome, 'html.parser')

        for div in titleurlsoup.body.find_all('div', class_=''):
            lyrics = div.text.strip().replace(",", ";")
            lyrics = re.sub(r'"', '', lyrics)
            lyrics = re.sub(r'[\t\r\n]', '|', lyrics)

        titlename = title.text.replace(",", ".")

        albumtype = albums[c].text.split(":", 1)[0]

        album_year = albums[c].text.split(":", 1)[1]

        album = re.findall(r'"(.*?)"', album_year)[0]

        year = album_year[album_year.find("(") + 1:album_year.find(")")]

        link = title['href'].replace("..", "http://www.azlyrics.com")

        time.sleep(random.choice([3, 4, 5, 6]))

        f.write(titlename.encode('ascii', 'ignore') + ", " + albumtype.encode('ascii', 'ignore') + ", " + album.encode('ascii', 'ignore') + ", " + year + ", " + link.encode('ascii', 'ignore') + ", " + lyrics.encode('ascii', 'ignore') + "\n")

        print titlename

    else:
        print " "
        c = c + 1

f.close()