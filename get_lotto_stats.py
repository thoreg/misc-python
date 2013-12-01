# -*- coding: utf-8 -*-
"""
Get statistics of all German lottery numbers and additional numbers

"""
import urllib2
from bs4 import BeautifulSoup
from pprint import pprint

URL = "http://www.lottozahlenonline.de/statistik/beide-spieltage/meistgezogene-lottozahlen.php"

try:
    page = urllib2.urlopen(URL).read()
except urllib2.HTTPError:
    print("HTTP Error")
except urllib2.URLError:
    print("URL Error")

soup = BeautifulSoup(page)
# print(soup.prettify())

number_of_frames = soup.findAll('div', attrs={'class':'h_zahlen_rahmen'})
print("We got %d values" % len(number_of_frames))

lotto_number_frames = number_of_frames[:49]
additional_number_frames = number_of_frames[49:]

result = {}
numbers = []
quantity = []
for frame in lotto_number_frames:
    numbers.append("%02s" % frame.findAll('div', attrs={'class':'h_zahlen_lottozahl'})[0].b.text)
    quantity.append(frame.findAll('div', attrs={'class':'h_zahlen_anzahl'})[0].text)

result['lotto_zahlen'] = zip(numbers, quantity)

numbers = []
quantity = []
for frame in additional_number_frames:
    numbers.append("%02s" % frame.findAll('div', attrs={'class':'h_zahlen_lottozahl'})[0].b.text)
    quantity.append(frame.findAll('div', attrs={'class':'h_zahlen_anzahl'})[0].text)

result['zusatz_zahlen'] = zip(numbers, quantity)

print
print("Lottozahlen:")
pprint(sorted(result['lotto_zahlen'], key=lambda v: v[1]))
print
print("Zusatzzahlen:")
pprint(sorted(result['zusatz_zahlen'], key=lambda v: v[1]))
