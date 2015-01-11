#!/usr/bin/env python

__author__ = 'seckcoder'

import sys
import json
import re
from datetime import datetime
import calendar

regexp_nonalphanum = "[^a-zA-Z0-9]+"
regexp_alphanum = "[a-zA-Z0-9]+"
regexp_nonalphanum_group = "(" + regexp_nonalphanum + ")"


def transTime(created_at):
    time_input_format = "%a %b %d %H:%M:%S  %Y"
    time_output_format = "%Y-%m-%d %H:%M:%S"
    created_at_no_tz = re.sub(r"[+-]([0-9])+", "", created_at)
    return datetime.strptime(created_at_no_tz, time_input_format).strftime(time_output_format)

for line in sys.stdin:
    line = line.strip()
    if line:
        tweet = json.loads(line)
        tweet_id_str = tweet["id_str"]
        created_at = transTime(tweet['created_at'])
        if tweet["place"] and tweet["place"]["name"]:
            location = tweet["place"]["name"]
        else:
            location = tweet["user"]["time_zone"]
            if not location:
                location = ''
            elif re.match(".*\stime\s.*", location.lower()):
                location = ''
        if location:
            if tweet["entities"]["hashtags"]:
                hashlist = []
                for tag in tweet["entities"]["hashtags"]:
                    hash_tags = tag["text"]
                    hash_index = str(tag["indices"][0])
                    if not hash_tags in hashlist:
                        hashlist.append(hash_tags)
                        print ('\t'.join([tweet_id_str,created_at,hash_tags,hash_index,location])).encode('utf-8')
