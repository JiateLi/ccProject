#!/usr/bin/python
#andrew ID:jiatel Name:Jiate Li email:lijiate1992@gmail.com
import operator#for sorting
f = open("output",'r')
y = open("finalreport.txt",'w')
orilist = []
rownum = 0#count the number of lines emerged in my output files
daystore = [0]*31
daysort = [0]*31
count = 0#count the number of days when views of "Google" is bigger than "Amazon.com"
Googlestore = [0]*31 #store the each day's views of article"Google"
Amazonstore = [0]*31#store the each day's views of article"Amazon.com"
monofAri = 0
maxnumofAri = 0
monofSca = 0
maxnumofSca = 0
monofDwa = 0
maxnumofDwa = 0
monofIgg = 0
maxnumofIgg = 0
monofKur = 0
maxnumofKur = 0

#function <getSumView> returns the total number of views when given an article
def getSumView(a,name):
    if a == 0:
        if linesp[1] == name:
            a = linesp[0]
    return a    


#function <getMaxView> returns the maximum number of views when given an article
def getMaxView(a,name):
    if a == 0:
        if linesp[1] == name:
            for i in range(3,64,2):
                daysort[((i-3)/2)]=int(linesp[i])
            daysort.sort()
            a = daysort[30]
    return a


while True:
    line = f.readline() 
    if len(line) == 0:  
        break
    rownum = rownum + 1
    linesp=line.split()
    monofAri = getSumView(monofAri,'Ariana_Grande')
    maxnumofAri = getMaxView(maxnumofAri,'Ariana_Grande')
    monofSca = getSumView(monofSca,'Scarlett_Johansson')
    maxnumofSca = getMaxView(maxnumofSca,'Scarlett_Johansson')
    monofDwa = getSumView(monofDwa,'Dwayne_Johnson')
    maxnumofDwa = getMaxView(maxnumofDwa,'Dwayne_Johnson')
    monofIgg = getSumView(monofIgg,'Iggy_Azalea')
    maxnumofIgg = getMaxView(maxnumofIgg,'Iggy_Azalea')
    monofKur = getSumView(monofKur,'Kurt_Russell')
    maxnumofKur = getMaxView(maxnumofKur,'Kurt_Russell')
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
    linesp[0] = int(linesp[0])
    orilist.append(linesp)


print('There are %s lines emerged in my output files' %(rownum))
print('The total views of Ariana_Grande is %s' %(monofAri))
print('The single-day maximum views of Ariana_Grande is %s' %(maxnumofAri))
print('The total views of Scarlett_Johansson is %s' %(monofSca))
print('The single-day maximum views of Scarlett_Johansson is %s' %(maxnumofSca))
print('The total views of Dwayne_Johnson is %s' %(monofDwa))
print('The single-day maximum views of Dwayne_Johnson is %s' %(maxnumofDwa))
print('The total views of Iggy_Azalea is %s' %(monofIgg))
print('The single-day maximum views of Iggy_Azalea is %s' %(maxnumofIgg))
print('The total views of Kurt_Russell is %s' %(monofKur))
print('The single-day maximum views of Kurt_Russell is %s' %(maxnumofKur))
print('The date when Dawn_of_the_Planet_of_the_Apes is %s' %(maxdayofDaw))


for i in range(0,31):
    if(Googlestore[i] > Amazonstore[i]):
        count = count+1
print('There are %s days that the view of Google larger than Amazon.com' %count)

#get the most popular article and its view
orilist.sort(key=lambda x:x[0],reverse=True)
for item in orilist:
    y.write("%s\t%s\n" %(item[0],item[1])) 
f.close()
y.close()
y = open('finalreport.txt','r')
line = y.readline()
linesp = line.split()
print('%s is the most popular article' %(linesp[1]))
print('Its total views is %s' %linesp[0])

