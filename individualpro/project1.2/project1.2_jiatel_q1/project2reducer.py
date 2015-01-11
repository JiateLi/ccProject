#!/usr/bin/python
#andrew id:jiatel Name:JiateLi email:lijiate1992@gmail.com
import sys#for getting the input of system
current_word = None
word = None
sumview = 0
#input comes from maper
for line in sys.stdin:
  line = line.strip()
  words = line.split()
  word = words[0]
  count = words[2]
  filename = words[1]
  namesp = filename.split('-')
  day = int(namesp[1]) % 100
  try:
    count = int(count)
  except ValueError:
    continue

  if current_word == word:
        sumview += count
        daysum[int(day-1)] += count
  else:
     if current_word:
        if int(sumview) > 100000:
            #output logs whose total views is bigger than 100000 with required style 
            print '%s\t%s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s' % (sumview,current_word,'date1',daysum[0],'date2',daysum[1],'date3',daysum[2],'date4',daysum[3],'date5',daysum[4],'date6',daysum[5],'date7',daysum[6],'date8',daysum[7],'date9',daysum[8],'date10',daysum[9],'date11',daysum[10],'date12',daysum[11],'date13',daysum[12],'date14',daysum[13],'date15',daysum[14],'date16',daysum[15],'date17',daysum[16],'date18',daysum[17],'date19',daysum[18],'date20',daysum[19],'date21',daysum[20],'date22',daysum[21],'date23',daysum[22],'date24',daysum[23],'date25',daysum[24],'date26',daysum[25],'date27',daysum[26],'date28',daysum[27],'date29',daysum[28],'date30',daysum[29],'date31',daysum[30])
     sumview = count
     current_word = word
     daysum = [0]*31
     daysum[int(day-1)] += count
#output the last word
if current_word == word:
  if int(sumview) > 100000:
    print '%s\t%s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s\t%s: %s' % (sumview,current_word,'date1',daysum[0],'date2',daysum[1],'date3',daysum[2],'date4',daysum[3],'date5',daysum[4],'date6',daysum[5],'date7',daysum[6],'date8',daysum[7],'date9',daysum[8],'date10',daysum[9],'date11',daysum[10],'date12',daysum[11],'date13',daysum[12],'date14',daysum[13],'date15',daysum[14],'date16',daysum[15],'date17',daysum[16],'date18:',daysum[17],'date19',daysum[18],'date20',daysum[19],'date21',daysum[20],'date22',daysum[21],'date23',daysum[22],'date24',daysum[23],'date25',daysum[24],'date26',daysum[25],'date27',daysum[26],'date28',daysum[27],'date29',daysum[28],'date30',daysum[29],'date31',daysum[30])
