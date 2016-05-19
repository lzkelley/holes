#!/usr/local/bin/python3.5
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import re

# Suspect catalog
response = urllib.request.urlopen('http://www.nhn.ou.edu/cgi-bin/cgiwrap/~suspect/snindex.cgi')

soup = BeautifulSoup(response.read(), "html5lib")
i = 0
for a in soup.findAll('a'):
    if 'phot=yes' in a['href'] and not 'spec=yes' in a['href']:
        if int(a.contents[0]) > 0:
            i = i + 1
            photlink = 'http://www.nhn.ou.edu/cgi-bin/cgiwrap/~suspect/' + a['href']
            eventresp = urllib.request.urlopen(photlink)
            eventtxt = eventresp.read().decode(eventresp.headers.get_content_charset())
            eventsoup = BeautifulSoup(eventtxt, "html5lib")
            ei = 0
            for ea in eventsoup.findAll('a'):
                if ea.contents[0] == 'I':
                    ei = ei + 1
                    bandlink = 'http://www.nhn.ou.edu/cgi-bin/cgiwrap/~suspect/' + ea['href']
                    bandresp = urllib.request.urlopen(bandlink)
                    bandtxt = bandresp.read().decode(bandresp.headers.get_content_charset())
                    bandsoup = BeautifulSoup(bandtxt, "html5lib")
                    if ei == 1:
                        names = bandsoup.body.findAll(text=re.compile("Name"))
                        name = 'SN' + names[0].split(':')[1].strip()
                    bands = bandsoup.body.findAll(text=re.compile("^Band"))
                    band = bands[0].split(':')[1].strip()
                    print ('../sne-external/SUSPECT/suspect-' + name + '-' + str(ei).zfill(2) + '-' + band + '.html')
                    with open('../sne-external/SUSPECT/suspect-' + name + '-' + str(ei).zfill(2) + '-' + band + '.html', 'w') as f:
                        f.write(bandtxt)
