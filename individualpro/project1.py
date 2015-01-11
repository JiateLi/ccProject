#!/usr/bin/python
#Project1.1 of cloud computing
import re
import operator
#import time
#starttime = time.clock()                #compute the time to execute this program
f = open("pagecounts-20140701-000000",'r')#open the wiki data
y = open("finalreport.txt",'w')         #open the file where we will write the final data
#counter = 0                             #count the number of final data
#orinum = 0
#sumrequest = 0
orilist = []#use to store final data and then sort them
while True:
        line = f.readline()             #read file line by line
        if len(line) == 0:              #if it is end of the file then break
                break
#        orinum = orinum + 1
        linesp=line.split()             #split each record into a list,in this case linesp[0] is project name,linesp[1] is page title, linesp[2] is number of access, linesp[3] is total bytes
#        sumrequest = sumrequest + int(linesp[2])
        if (linesp[0] == "en"):         #filter non-english records
                matchObj1 = re.compile(r'^Media:|^Special:|^Talk:|^User:|^User_talk:|^Project:|^Project_talk:|^File:|^File_talk:|^MediaWiki:|^MediaWiki_talk:|^Template:|^Template_talk:|^Help:|^Help_talk:|^Category:|^Category_talk:|^Portal:|^Wikipedia:|^Wikipedia_talk:')#set the match pattern of rule2, "^" means match front of the string  
                if not matchObj1.search(linesp[1]):                     #filter records start with above string
                    matchObj1 = re.match(r'[a-z]', linesp[1])           #"match" is more convient, this line finds records whose article titles start with lowercase characters
                    if not matchObj1:
                        matchObj2 = re.findall(r'\.jpg|\.gif|\.png|\.JPG|\.GIF|\.PNG|\.txt|\.ico\Z', linesp[1])#use "\" as a escape character that keep "." as a part of string, then filter records whose article titles end with these string
                        if not matchObj2:
                            if not((linesp[1] == "404_error/") | (linesp[1] == "Main_Page") | (linesp[1] == "Hypertext_Transfer_Protocol") | (linesp[1] == "Favicon.ico") | (linesp[1] == "Search")):#rule 5:filter records whose article titles match these strings
                                linesp[2] = int(linesp[2])                      #transfer from string to interger, which helps sort the records
                                orilist.append(linesp)                          #append all retained records to orlist
#                                counter = counter + 1  
orilist.sort(key=lambda x:x[2],reverse=True)                                    #sort the records in orilist using lambda
for item in orilist:
    y.write("%s\t%s\n" %(item[1],item[2]))                                      #write article titles and article views of records in new file
y.close() #close files
f.close()

#print("The number of lines in the original file is:")
#print(orinum)
#print("The total number of all requests is:")
#print(sumrequest)
#print("The number of log after filtering is:")
#print(counter)
#y = open("finalreport.txt",'r')#find out the most popular article
#line = y.readline()
#aftersplit = line.split()
#print("The most popular article is:")
#print(aftersplit[0])
#print("The number of view is:")
#print(aftersplit[1])
#endtime = time.clock()
#print("The running time of this program is:")
#print(endtime-starttime)
