import bs4 as bs
import urllib2

titleurl = 'http://www.azlyrics.com/lyrics/coldplay/onlysuperstition.html'

titlehome = urllib2.urlopen(titleurl)

titleurlsoup = bs.BeautifulSoup(titlehome,'html.parser')


for div in titleurlsoup.body.find_all('div', class_=''):
    lyrics = div.text.strip().replace(",", "|")


print lyrics