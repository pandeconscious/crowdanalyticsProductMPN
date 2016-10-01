'''
Created on 30-Sep-2016

@author: harshit
'''

import pandas as pd

train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

train_data_mpn = train_data['mpn_qs'].astype(str)

charCountMap = {}
firstCharCountMap = {}
lastCharCountMap = {}

for mpn in train_data_mpn:
    for ch in mpn:
        oldVal = charCountMap.get(ch)
        
        if oldVal == None:
            charCountMap[ch] = 1
        else:
            charCountMap[ch] = oldVal + 1
    
    oldVal = firstCharCountMap.get(mpn[0])
    if oldVal == None:
        firstCharCountMap[mpn[0]] = 1
    else:
        firstCharCountMap[mpn[0]] = oldVal + 1
    
    oldVal = lastCharCountMap.get(mpn[-1])
    if oldVal == None:
        lastCharCountMap[mpn[-1]] = 1
    else:
        lastCharCountMap[mpn[-1]] = oldVal + 1
    
        

f = open('../aux_data/train_mpn_char_counts.txt','w')

import operator
sortedByCounts = sorted(charCountMap.items(), key=operator.itemgetter(1))

for ch, count in sortedByCounts:
    f.write(ch + " ==> " + str(count) + '\n')
    

f = open('../aux_data/train_mpn_first_char_counts.txt','w')

sortedByCounts = sorted(firstCharCountMap.items(), key=operator.itemgetter(1))

for ch, count in sortedByCounts:
    f.write(ch + " ==> " + str(count) + '\n')


f = open('../aux_data/train_mpn_last_char_counts.txt','w')

sortedByCounts = sorted(lastCharCountMap.items(), key=operator.itemgetter(1))

for ch, count in sortedByCounts:
    f.write(ch + " ==> " + str(count) + '\n')

char_not_first = set(charCountMap.keys()) - set(firstCharCountMap.keys())
print "chars not present at first position"
print char_not_first

char_not_last = set(charCountMap.keys()) - set(lastCharCountMap.keys())
print "chars not present at last position"
print char_not_last

    
