import bs4 as bs
import urllib2

# artist = 'u/u2'
# firstothertitle = "11 O'Clock Tick Tock"

artist = 'c/coldplay'
firstothertitle = "1.36"


artisturl = 'http://www.azlyrics.com/' + artist +'.html'

artisthome = urllib2.urlopen(artisturl)

soup = bs.BeautifulSoup(artisthome,'html.parser')

titlelists= soup.body.find(id = "listAlbum")

albums = soup.body.find_all('div', class_='album')

titles = titlelists.find_all('a')

c = 0
for title in titles[1:]:
    if (title.text) == firstothertitle:
        c = c + 1
        print " "
    if (title.text.strip()) != '':
        print (title.text.replace (",",".")) + ", " + (albums[c].text) + ", " + (title['href'].replace("..","http://www.azlyrics.com"))
    else:
        print " "
        c = c + 1








