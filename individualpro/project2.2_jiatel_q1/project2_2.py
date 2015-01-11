#!/usr/bin/python
#encoding=utf8
#andrew id: jiatel
#Project2.2 of cloud computing
import boto.ec2.elb#to connect to and create ec2 elb
import boto.ec2.autoscale#to connect to and create ec2 autoscale
import boto.ec2.cloudwatch#to connect to and create ec2 cloudwatch
import boto.ec2 #to use ec2
import urllib2 #to open and read url
import time#to set sleep time
from boto.ec2.elb import HealthCheck#to create ec2 elb's Healthcheck
from boto.ec2.autoscale import AutoScaleConnection#to create an ec2 autoscale connection
from boto.ec2.autoscale import LaunchConfiguration#to create an ec2 elb launch configuration
from boto.ec2.autoscale import AutoScalingGroup#to create an autoscaling group
from boto.ec2.autoscale import ScalingPolicy#to create scaling policy
from boto.ec2.cloudwatch import MetricAlarm# to set alarm




#-----------------------launch an elb-------------------------------#
conn = boto.ec2.elb.connect_to_region('us-east-1')
zones = ['us-east-1a','us-east-1b']
ports = [(80,80,'http')]

hc = HealthCheck(
	interval = 30,
	healthy_threshold = 3,
	unhealthy_threshold = 5,
	target = 'HTTP:80/heartbeat?username=jiatel'
	)

lb = conn.create_load_balancer('my-lb',zones,ports)
lb.configure_health_check(hc)

time.sleep(15)
elbdns = lb.dns_name


#---------------------------create autoscaling group and set the configuration-----------#
autoconn = boto.ec2.autoscale.connect_to_region('us-east-1')

lc = LaunchConfiguration(
	name = 'my-launch_config',
	image_id = 'ami-ec14ba84',
	key_name = '15619project',
	instance_type = 'm3.medium',  
	instance_monitoring = True, 
	security_groups = ['launch-wizard-12'])

autoconn.create_launch_configuration(lc)
time.sleep(18)

ag = AutoScalingGroup(
	group_name = 'my_group',
	load_balancers = ['my-lb'],
	availability_zones = ['us-east-1a'],
	launch_config = lc,
	min_size = 3,
	max_size = 5,
	desired_capacity = 3,
	connection = autoconn,
	tags = [boto.ec2.autoscale.tag.Tag(key='Project',value='2.2',resource_id='my_group',propagate_at_launch = True)]
	)

time.sleep(20)

autoconn.create_auto_scaling_group(ag)

time.sleep(20)

#------------------------create the load generator -------------------------------#
load_conn = boto.ec2.connect_to_region("us-east-1")  
loadGe = load_conn.run_instances(
        'ami-562d853e',
        key_name = '15619project',
        instance_type = 'm3.medium',
        security_groups = ['launch-wizard-12'])

#wait for the load generator begins to run and tag it then get its dns
status = loadGe.instances[0].update()
while status == 'pending':
    time.sleep(5)
    status = loadGe.instances[0].update()

if status == 'running':
    loadGe.instances[0].add_tag("Project","2.2")
    instance_id = loadGe.instances[0].id
    researvation = load_conn.get_all_instances(instance_ids = [instance_id])
    insLoad = researvation[0].instances[0]
else:
    print('Instance status: ' + status)

time.sleep(60)#wait the load generator finishes the process of booting up

url_act_load = "http://" + insLoad.public_dns_name + "/username?username=jiatel"
url_warmup = "http://" + insLoad.public_dns_name + "/warmup?dns=" + elbdns + "&testId=echoj"
url_warmlog = "http://" + insLoad.public_dns_name + "/view-logs?name=warmup_jiatel.txt"
url_test = "http://" + insLoad.public_dns_name + "/begin-phase-2?dns=" + elbdns + "&testId=echoj"

urllib2.urlopen(url_act_load)    

time.sleep(100)



#------------------------ the function warmUp is used to warm up the instance --------------#
def warmUp():
	urllib2.urlopen(url_warmup)
	while 1:
		time.sleep(3)
		warmcon = urllib2.urlopen(url_warmlog).read()
		print warmcon
		length = len(warmcon.split("\n"))
		if (length > 8):#when warmup finished there are 9 rows in the log page
			break
	print("warmup finished")

#--------------------------------------------------------------------------------------------#

warmUp()
warmUp()
warmUp()

#Once your ELB is warmed up, start the test by visiting the URL
urllib2.urlopen(url_test) 


#------------------------------ set up the policy and alarm ---------------------#
#set up scale up policy and scale down policy
scale_up_policy = ScalingPolicy(
	name = 'scale_up',
	adjustment_type = 'ChangeInCapacity',
	as_name = 'my_group',
	scaling_adjustment = 2,
	cooldown = 180)

scale_down_policy = ScalingPolicy(
	name = 'scale_down',
	adjustment_type = 'ChangeInCapacity',
	as_name = 'my_group',
	scaling_adjustment = -2,
	cooldown = 180)

time.sleep(240)#set the policy 4 minutes after starting the test, prevents the DDOS appears in the beginning

autoconn.create_scaling_policy(scale_up_policy)
autoconn.create_scaling_policy(scale_down_policy)

scale_up_policy = autoconn.get_all_policies(
	as_group = 'my_group',
	policy_names = ['scale_up'])[0]

scale_down_policy = autoconn.get_all_policies(
	as_group = 'my_group',
	policy_names = ['scale_down'])[0]

cloudwatch = boto.ec2.cloudwatch.connect_to_region('us-east-1')

alarm_dimensions = {"AutoScalingGroupName": 'my_group'}

scale_up_alarm = MetricAlarm(
	name = 'scale_up_on_cpu',
	namespace = 'AWS/EC2',
	metric = 'CPUUtilization',
	statistic = 'Average',
	comparison = '>',
	threshold = '90',
	period = '60',
	evaluation_periods = 3,
	alarm_actions = [scale_up_policy.policy_arn],
	dimensions = alarm_dimensions)

cloudwatch.create_alarm(scale_up_alarm)

scale_down_alarm = MetricAlarm(
	name = 'scale_down_on_cpu',
	namespace = 'AWS/EC2',
	metric = 'CPUUtilization',
	statistic = 'Average',
	comparison = '<',
	threshold = '60',
	period = '60',
	evaluation_periods = 2,
	alarm_actions = [scale_down_policy.policy_arn],
	dimensions = alarm_dimensions)

cloudwatch.create_alarm(scale_down_alarm)

time.sleep(2400)#test end


#----------------------------- terminate all things -----------------------#
ag.shutdown_instances()
ag.delete()
lc.delete()