#!/usr/bin/env python3

import csv
list = []
with open('MyEBirdData.csv', mode = 'r') as file:
    csvfile = csv.DictReader(file)
    for lines in csvfile:
        list.append(lines)
dict = {}
for l in list:
    if l['Common Name'] in dict and dict[l['Common Name']] == False:
        if l['ML Catalog Numbers'] != None:
            dict[l['Common Name']] = True
    elif not(l['Common Name'] in dict):
        dict[l['Common Name']] = (l['ML Catalog Numbers'] != None)

listnophoto=[]
for key in dict:
    if dict[key]== False:
        listnophoto.append(key)

print(listnophoto)
print(len(listnophoto))
print(107-83)
