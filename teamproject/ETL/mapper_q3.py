#!/usr/bin/env python

import sys
import json
import re

for line in sys.stdin:
    line = line.strip()
    if line:
        tweet = json.loads(line)
        user_id_str = tweet["user"]["id_str"]
        if tweet.has_key("retweeted_status"):
            retweeted_status = tweet["retweeted_status"]
            orig_user_id_str = retweeted_status["user"]["id_str"]
            print ("%s\t%s" %(user_id_str,orig_user_id_str))
