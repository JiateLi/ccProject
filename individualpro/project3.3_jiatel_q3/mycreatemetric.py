#!/usr/bin/python
# encoding: utf-8
import boto
import boto.ec2
import boto.ec2.elb
import boto.ec2.cloudwatch
from boto.ec2.elb import HealthCheck
import time
import os
import sys
num_thread = 16#number of thread
max_TPS = 145.00#the max TPS
err_query = 6#error of query
qureyinfo = "/usr/bin/mysql -u root -pdb15319root --execute=\"show status like \'Queries\'\""
timeinfo = "/usr/bin/mysql -u root -pdb15319root --execute=\"show status like \'Uptime\'\""
key_id = 'AKIAJ5ZAQDGB4NAWQDRA'
secret_key = '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'

def getinfo(content):
        readmysql = os.popen(content).read()
        splinfo = readmysql.split()
        info = int(splinfo[3])
        #print info
        return info

cw_conn = boto.ec2.cloudwatch.CloudWatchConnection(
        aws_access_key_id = key_id, 
        aws_secret_access_key = secret_key)

lastquery = getinfo(qureyinfo)
lasttime = getinfo(timeinfo)
time.sleep(60)

while(True):
        curquery = getinfo(qureyinfo) - err_query
        curtime = getinfo(timeinfo)
        real_tps = (curquery - lastquery)/(curtime - lasttime)/num_thread
        tpsuti = real_tps * 100/max_TPS
        #print tpsuti
        lastquery = curquery
        lasttime = curtime
        cw_conn.put_metric_data(
                namespace = "myMetric",
                name = "TPS",
                value = tpsuti,
                unit = 'Percent')
        time.sleep(60)
