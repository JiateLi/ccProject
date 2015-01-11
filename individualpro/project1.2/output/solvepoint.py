#!/usr/bin/python
#andrew ID:jiatel Name:Jiate Li email:lijiate1992@gmail.com
import operator
f = open("output",'r')#open the wiki data
y = open("finalreport.txt",'w')
orilist = []
rownum = 0#count the number of lines emerged in my output files
daystore = [0]*31
daysort = [0]*31
count = 0#count the number of days when views of "Google" is bigger than "Amazon.com"
Googlestore = [0]*31 #store the each day's views of article"Google"
Amazonstore = [0]*31#store the each day's views of article"Amazon.com"
while True:
    line = f.readline() 
    if len(line) == 0:  
        break
    rownum = rownum + 1
    linesp=line.split()
    if linesp[1] == 'The_Fault_in_Our_Stars_(film)':
        monofThe = linesp[0]
        for i in range(3,64,2):
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofThe = daysort[30]
    if linesp[1] == 'Guardians_of_the_Galaxy_(film)':
        monofGua = linesp[0]
        for i in range(3,64,2):
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofGua = daysort[30]
    if linesp[1] == 'Maleficent_(film)':
        monofMal = linesp[0]
        for i in range(3,64,2):
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofMal = daysort[30]
    if linesp[1] == 'Gravity_(film)':
        monofGra = linesp[0]
        for i in range(3,64,2):
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofGra = daysort[30]
    if linesp[1] == 'Her_(film)':
        monofHer = linesp[0]
        for i in range(3,64,2):
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofHer = daysort[30]
    if linesp[1] == 'Google':
        for i in range(3,64,2):
            Googlestore[((i-3)/2)]=int(linesp[i])
    if linesp[1] == 'Amazon.com':
        for i in range(3,64,2):
            Amazonstore[((i-3)/2)]=int(linesp[i])
    if linesp[1] == 'Dawn_of_the_Planet_of_the_Apes':
        for i in range(3,64,2):
            daystore[((i-3)/2)]=int(linesp[i])
            daysort[((i-3)/2)]=int(linesp[i])
        daysort.sort()
        maxnumofDaw = daysort[30]
        maxdayofDaw = daystore.index(maxnumofDaw)+1
    orilist.append(linesp)
print('There are %s lines emerged in my output files' %(rownum))
print('The total views of The_Fault_in_Our_Stars_(film) is %s' %(monofThe))
print('The single-day maximum views of The_Fault_in_Our_Stars_(film) is %s' %(maxnumofThe))
print('The total views of Guardians_of_the_Galaxy_(film) is %s' %(monofGua))
print('The single-day maximum views of Guardians_of_the_Galaxy_(film) is %s' %(maxnumofGua))
print('The total views of Maleficent_(film) is %s' %(monofMal))
print('The single-day maximum views of Maleficent_(film) is %s' %(maxnumofMal))
print('The total views of Gravity_(film) is %s' %(monofGra))
print('The single-day maximum views of Gravity_(film) is %s' %(maxnumofGra))
print('The total views of Her_(film) is %s' %(monofHer))
print('The single-day maximum views of Her_(film) is %s' %(maxnumofHer))
print('The date when Dawn_of_the_Planet_of_the_Apes is %s' %(maxdayofDaw))
for i in range(0,31):
    if(Googlestore[i]>Amazonstore[i]):
        count = count+1
print('There are %s days that the view of Google larger than Amazon.com' %count)
orilist.sort(key=lambda x:x[0],reverse=True)
for item in orilist:
    y.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(item[0],item[1],item[3],item[5],item[7],item[9],item[11],item[13],item[15],item[17],item[19],item[21],item[23],item[25],item[27],item[29],item[31],item[33],item[35],item[37],item[39],item[41],item[43],item[45],item[47],item[49],item[51],item[53],item[55],item[57],item[59],item[61],item[63])) 
f.close()
y.close()
y = open('finalreport.txt','r')
line = y.readline()
linesp=line.split()
print('%s is the most popular article' %(linesp[1]))
print('Its total views is %s' %linesp[0])

