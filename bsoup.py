import bs4 as bs
import urllib2

artist = 'c/coldplay'

artisturl = 'http://www.azlyrics.com/' + artist +'.html'

artisthome = urllib2.urlopen(artisturl)

soup = bs.BeautifulSoup(artisthome,'lxml')

songlists= soup.body.find(id = "listAlbum")

for link in songlists.find_all('a'):
    #print (link.get('href'))
    print (link.text)

for div in soup.body.find_all('div', class_='album'):
    print div.b


