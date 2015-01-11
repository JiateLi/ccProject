#!/usr/bin/env python

import sys
import json
import re
from datetime import datetime
import calendar

regexp_nonalphanum = "[^a-zA-Z0-9]+"
regexp_alphanum = "[a-zA-Z0-9]+"
regexp_nonalphanum_group = "(" + regexp_nonalphanum + ")"

def rot13(s):
    def ccUpper(c):
        if 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + 13)%26 + ord('A'))
        else:
            return False
    def ccLower(c):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + 13)%26 + ord('a'))
        else:
            return False
    def anyc(c):
        return c
    def combine(*fs):
        def inner(c):
            for f in reversed(fs):
                v = f(c)
                if v: return v
        return inner
    transform = combine(anyc, ccLower, ccUpper)
    return ''.join(transform(c) for c in s)



def getSCore(words_vec, afinn_dict):
    return sum(afinn_dict.get(w.lower(), 0) for w in words_vec)

def censor(word, banned_text_set):
    if word.lower() in banned_text_set and len(word) > 2:
        return word[0] + '*'*(len(word)-2) + word[-1]
    else:
        return word

def getCensoredText(words_vec, banned_text_set):
    return ''.join(censor(w, banned_text_set) for w in words_vec)

def loadAFINN():
    with open('./AFINN_cached.txt', 'r') as fin:
        d = {}
        for line in fin:
            line = line.strip()
            if line:
                word, score = line.split('\t')
                # print word,'\t*****\t', score
                d[word] = int(score)
        return d

def loadBannedText():
    with open('./banned_cached.txt', 'r') as fin:
        s = set()
        for line in fin:
            line = line.strip()
            if line:
                s.add(rot13(line))
        return s
       

def testBannedText():
    with open('./banned_cached.txt') as fin:
        for line in fin:
            if line.strip():
                line = line.strip()
                print line, "\t", rot13(line)

def testRot():
    print rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


def Transformer():
    afinn_dict = loadAFINN()
    banned_text_set = loadBannedText()
    def inner(text):
        words_vec = re.split(regexp_nonalphanum_group, text)
        score = getSCore(words_vec, afinn_dict)
        cs_text = getCensoredText(words_vec, banned_text_set)
        return score, cs_text
    return inner

def transTime(created_at):
    time_input_format = "%a %b %d %H:%M:%S  %Y"
    created_at_no_tz = re.sub(r"[+-]([0-9])+", "", created_at) # skip timezone
    ts = calendar.timegm(datetime.strptime(created_at_no_tz, time_input_format).utctimetuple())
    return ts

def main():
    #time_output_format = "%Y-%m-%d+%H:%M:%S"
    trans = Transformer()
    for line in sys.stdin:
        line = line.strip()
        if line:
            tweet = json.loads(line)
            text = tweet['text']
            score, cs_text = trans(text)
            user_id_str = tweet["user"]["id_str"]
            tweet_id_str = tweet["id_str"]
            created_at = transTime(tweet['created_at'])
            print "%s\t%s\t%s\t%s\t%s" % (user_id_str, created_at, tweet_id_str, str(score), cs_text.encode('unicode-escape'))

main()
