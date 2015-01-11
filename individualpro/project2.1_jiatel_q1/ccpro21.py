#!/usr/bin/python
#encoding=utf8
#andrew id: jiatel
#Project2.1 of cloud computing
import boto.ec2 #to use ec2
import urllib2 #to open and read url
import time#to set sleep time
import re#to use regular expression

Addmore = True#guarantee program runs when req<3600
minline = 1
numofIns = 0#number of instance
maxline = 0
sumreq = 0#sum of requests of all instances

#fuction newdace() is used to launch a new data center and activate it
def newdace():
    dataCe = conn.run_instances(
        'ami-324ae85a',
        key_name = '15619project',
        instance_type = 'm3.medium',
        security_groups = ['launch-wizard-12'])

    time.sleep(60)
    dataCe.instances[0].add_tag("Project","2.1")
    instance_id = dataCe.instances[0].id
    researvation = conn.get_all_instances(instance_ids = [instance_id])
    insData = researvation[0].instances[0]
    url1 = "http://" + insLoad.public_dns_name + "/username?username=jiatel"
    try:
        urllib2.urlopen(url1,timeout = 10)
    except:
        print("error1!")
    url2 = "http://" + insData.public_dns_name + "/username?username=jiatel"
    try:
        urllib2.urlopen(url2,timeout = 10)
    except:
        print("error2!")
    url3 = "http://" + insLoad.public_dns_name + "/part/one/i/want/more?dns=" + insData.public_dns_name + "&testId=Echoli"
    try:
        urllib2.urlopen(url3,timeout = 10)
    except:
        print("error3!")



conn = boto.ec2.connect_to_region("us-east-1")  
loadGe = conn.run_instances(
        'ami-1810b270',
        key_name = '15619project',
        instance_type = 'm3.medium',
        security_groups = ['launch-wizard-12'])


status = loadGe.instances[0].update()
while status == 'pending':
    time.sleep(10)
    status = loadGe.instances[0].update()

if status == 'running':
    loadGe.instances[0].add_tag("Project","2.1")
    instance_id = loadGe.instances[0].id
    researvation = conn.get_all_instances(instance_ids = [instance_id])
    insLoad = researvation[0].instances[0]
else:
    print('Instance status: ' + status)



newdace()
numofIns = numofIns + 1
maxline = minline + numofIns
time.sleep(150)#wait for the log web shows 2 min's content
while Addmore:
    url4="http://"+insLoad.public_dns_name+"/view-logs?name=result_jiatel_Echoli.txt"
    try:
        connect = urllib2.urlopen(url4).read()
    except:
        print("error4!")
    print(connect)
    data = connect.split("\n")
    mylist = []
    pattern = re.compile(r'^ec2')
    
    for i in data:
        if pattern.search(i):
            mylist.append(i)
    
    for j in range(minline,maxline,1):#get all instances' request in this minute
        info = mylist[j].split()
        sumreq = sumreq + float(info[4])

    if (sumreq < 3600):
        newdace()
        numofIns = numofIns + 1
        sumreq = 0
    else:
        Addmore = False
        break
    
    time.sleep(150)
    minline = minline + 3#about 3 minutes update sumreq 
    maxline = minline + numofIns

