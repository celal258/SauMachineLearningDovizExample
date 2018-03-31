"""
Created on Mon Mar 26 04:13:59 2018

@author: celal258
"""

import requests

from html.parser import HTMLParser
import xml.etree.ElementTree as ET

parseAttr=[]
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag=="a"):
            for attr in attrs:
                parseAttr.append(attr[1])

parser = MyHTMLParser()
r = requests.get('http://www.tcmb.gov.tr/kurlar/kur2013_tr.html')#Aylarin linklerinin olduğu sayfa
parser.feed(r.text)
monthAttr=[]
monthAttr=parseAttr.copy()#a tag'dan faydalanarak linkleri alıyor.
parseAttr.clear()#dizi tekrar kullanılmak üzere boşaltılıyor.
f = open('data.csv', 'w') 
f.write('Tarih,Doviz Alis,Doviz Satis,Efektif Alis,Efektif Satis\n');
for moth in monthAttr:
    print('http://www.tcmb.gov.tr/kurlar/'+str(moth))
    r = requests.get('http://www.tcmb.gov.tr/kurlar/'+str(moth))
    parser.feed(r.text)#Ayın hesaplanan günleri çekiliyor.
    for parse in parseAttr:
        dovizxml = requests.get('http://www.tcmb.gov.tr'+parse)
        root = ET.fromstring(dovizxml.text)
        tarih=(((str(root.attrib)[1:-1]).split(',')[2].split(':')[1])[2:-1])
        try:
            #Tarih kismi ay/gun seklinde tabloya cekilmistir. 
            f.write(tarih.split('.')[1]+tarih.split('.')[0]+','+str(root[0][3].text)+','+str(root[0][4].text)+','+str(root[0][5].text)+','+str(root[0][6].text)+'\n')
        except :
            print("Hatalı Çekme İşlemi")
    parseAttr.clear()
f.close()
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 04:13:59 2018

@author: celal258
"""

import requests

from html.parser import HTMLParser
import xml.etree.ElementTree as ET

parseAttr=[]
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag=="a"):
            for attr in attrs:
                parseAttr.append(attr[1])

parser = MyHTMLParser()
r = requests.get('http://www.tcmb.gov.tr/kurlar/kur2013_tr.html')#Aylarin linklerinin olduğu sayfa
parser.feed(r.text)
monthAttr=[]
monthAttr=parseAttr.copy()#a tag'dan faydalanarak linkleri alıyor.
parseAttr.clear()#dizi tekrar kullanılmak üzere boşaltılıyor.
f = open('data.csv', 'w') 
f.write('Tarih,Doviz Alis,Doviz Satis,Efektif Alis,Efektif Satis\n');
for moth in monthAttr:
    print('http://www.tcmb.gov.tr/kurlar/'+str(moth))
    r = requests.get('http://www.tcmb.gov.tr/kurlar/'+str(moth))
    parser.feed(r.text)#Ayın hesaplanan günleri çekiliyor.
    for parse in parseAttr:
        dovizxml = requests.get('http://www.tcmb.gov.tr'+parse)
        root = ET.fromstring(dovizxml.text)
        tarih=(((str(root.attrib)[1:-1]).split(',')[2].split(':')[1])[2:-1])
        try:
            f.write(tarih.split('.')[1]+tarih.split('.')[0]+','+str(root[0][3].text)+','+str(root[0][4].text)+','+str(root[0][5].text)+','+str(root[0][6].text)+'\n')
        except :
            print(tarih,root[0][3].text)
    parseAttr.clear()
f.close()
print('Bitti')