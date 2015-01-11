#!/usr/bin/python
#andrew id: jiatel Name:JiateLi email:lijiate1992@gmail.com
#Project1.2 of cloud computing
import sys#for reading system input
import os#for getting the filename within mapper
import re#for using Regular expression
import operator
filtList = []#for store logs which should be retained
for line in sys.stdin:
        line = line.strip()
        linesp=line.split()
        #filter non-english records
        if (linesp[0] == "en"):
                #filtering out log starts with following strings
                matchObj1 = re.compile(r'^Media:|^Special:|^Talk:|^User:|^User_talk:|^Project:|^Project_talk:|^File:|^File_talk:|^MediaWiki:|^MediaWiki_talk:|^Template:|^Template_talk:|^Help:|^Help_talk:|^Category:|^Category_talk:|^Portal:|^Wikipedia:|^Wikipedia_talk:')  
                if not matchObj1.search(linesp[1]):
                    matchObj1 = re.match(r'[a-z]', linesp[1])
                    if not matchObj1:
                        matchObj2 = re.findall(r'\.jpg|\.gif|\.png|\.JPG|\.GIF|\.PNG|\.txt|\.ico\Z', linesp[1])
                        if not matchObj2:
                            if not((linesp[1] == "404_error/") | (linesp[1] == "Main_Page") | (linesp[1] == "Hypertext_Transfer_Protocol") | (linesp[1] == "Favicon.ico") | (linesp[1] == "Search")):
                                linesp[2] = int(linesp[2])
                                filepath = os.environ['map_input_file']
                                #get the filename
                                filename = os.path.split(filepath)[-1]
                                linesp.append(filename)
                                filtList.append(linesp) 
for item in filtList:
    print("%s\t%s\t%s" %(item[1],item[4],item[2]))   
