#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
#reader = csv.reader(open("week0.csv"))
data=[]
TPS=0
Hour=''
newTPS=0
def caltps(j):
    reader = csv.reader(open("week0.csv"))
    for i, rows in enumerate(reader):
        if i != 0:
            TPS = float(rows[1])
            Hour = rows[0]
            newTPS = str(TPS*((0.12*j/52)+1))
            newrow = [j,Hour,newTPS]
            data.append(newrow)

caltps(52)

#print data
with open('52week.csv','wb') as newfile:
    mywriter=csv.writer(newfile,dialect='excel')
    mywriter.writerow(['week','Hour','TPS'])
    mywriter.writerows(data)
