#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from urllib2 import urlopen
import bs4 as BeautifulSoup
import csv
import re

page = 'https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000032669529&dateTexte=&categorieLien=id'
page = 'http://localhost:8000/joCN.html'
html = urlopen(page).read()

soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')

aPageElements = soup.select("div ul li p")

i = 0
liste = []
for element in aPageElements:
    if (i%2==0):
        # print 'TITRE -- '
        #print element.text
        liste.append(element.text)
    else:
        # print 'Communes -- '
        # print element.text
        communes = element.text.split(', ')
        for commune in communes:
            liste.append(commune)

    i=i+1

#print liste


with open('communesCatastropheNatuelles.csv', 'wb') as csvfile:
    csvWriter = csv.writer(csvfile)
    try:
        for element in liste:
            # print element.encode('utf8')
            m = re.search(r"(.*) \((\d)\)", element.encode('utf8'), flags=re.U)
            if m == None :
                # Récupérer le département
                # DÉPARTEMENT DU CHERInondations et coulées de boue du 28 mai 2016 au 4 juin 2016

                aElements = element.split('Inondations')
                chaineDepartement = aElements[0].encode('utf8')
                print [chaineDepartement, 0]
                csvWriter.writerow([chaineDepartement, 0])
            else:
                commune = m.group(1)
                print [commune, int(m.group(2))]
                csvWriter.writerow([commune, int(m.group(2))])

    finally:
        #
        # Fermeture du fichier source
        #
        csvfile.close()

