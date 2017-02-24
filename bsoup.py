import bs4 as bs
import urllib2

# artist = 'u/u2'
# firstothersong = "11 O'Clock Tick Tock"

artist = 'c/coldplay'
firstothersong = "1.36"


artisturl = 'http://www.azlyrics.com/' + artist +'.html'

artisthome = urllib2.urlopen(artisturl)

soup = bs.BeautifulSoup(artisthome,'html.parser')

songlists= soup.body.find(id = "listAlbum")

albums = soup.body.find_all('div', class_='album')

songs = songlists.find_all('a')

c = 0
for song in songs[1:]:
    if (song.text) == firstothersong:
        c = c + 1
        print " "
    if (song.text.strip()) != '':
        print (song.text.replace (",",".")) + ", " + (albums[c].text) + ", " + (song['href'].replace("..","http://www.azlyrics.com"))
    else:
        print " "
        c = c + 1








