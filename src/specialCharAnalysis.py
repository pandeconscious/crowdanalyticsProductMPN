'''
Created on 02-Oct-2016

@author: harshit
'''

import pandas as pd
from nltk.corpus import words 
from nltk.corpus import gutenberg

charsToanalyse = "-./"

train_data = pd.read_csv('../data/CAX_Train.csv')
train_data_mpn = train_data['mpn_qs'].astype(str)

hyphenCountDistr = {}
dotCountDistr = {}
slashCountDistr = {}

countHyphenDotBoth = 0
countHyphenSlashBoth = 0
countDotSlashBoth = 0

singleHyphenCountBothSidesEngish = 0
singleDotCountBothSidesEngish = 0
singleSlashCountBothSidesEngish = 0

d = set(words.words())
dgtn = set(gutenberg.words())

for mpn in train_data_mpn:
    countHyphen = mpn.count('-')
    countDot = mpn.count('.')
    countSlash = mpn.count('/')
    
    oldVal = hyphenCountDistr.get(countHyphen)
    if oldVal == None:
        hyphenCountDistr[countHyphen] = 1
    else:
        hyphenCountDistr[countHyphen] = oldVal + 1
    
    if countHyphen == 1:
        left, right = mpn.split('-')
        if (left.lower() in d or left.lower() in dgtn) and (right.lower() in d or right.lower() in dgtn):
            singleHyphenCountBothSidesEngish += 1
            
    if countDot == 1:
        left, right = mpn.split('.')
        if (left.lower() in d or left.lower() in dgtn) and (right.lower() in d or right.lower() in dgtn):
            singleDotCountBothSidesEngish += 1
            
    if countSlash == 1:
        left, right = mpn.split('/')
        if (left.lower() in d or left.lower() in dgtn) and (right.lower() in d or right.lower() in dgtn):
            singleSlashCountBothSidesEngish += 1
       
    oldVal = dotCountDistr.get(countDot) 
    if oldVal == None:
        dotCountDistr[countDot] = 1
    else:
        dotCountDistr[countDot] = oldVal + 1
        
    oldVal = slashCountDistr.get(countSlash) 
    if oldVal == None:
        slashCountDistr[countSlash] = 1
    else:
        slashCountDistr[countSlash] = oldVal + 1
        
    if countHyphen > 0 and countDot > 0:
        countHyphenDotBoth += 1
    if countHyphen > 0 and countSlash > 0:
        countHyphenSlashBoth += 1
    if countDot > 0 and countSlash > 0:
        countDotSlashBoth += 1

print "\n===============hyphen================"
for k, v in hyphenCountDistr.iteritems():
    print k, v
    
print "\n===============dot================"
for k, v in dotCountDistr.iteritems():
    print k, v
    
print "\n===============slash================"
for k, v in slashCountDistr.iteritems():
    print k, v
    
print "hyphen-dot: ", countHyphenDotBoth
print "hyhen-slash: ", countHyphenSlashBoth
print "dot-slash: ", countDotSlashBoth

print "num of single hyphen mpns with both sides english: ", singleHyphenCountBothSidesEngish
print "num of single dot mpns with both sides english: ", singleDotCountBothSidesEngish
print "num of single slash mpns with both sides english: ", singleSlashCountBothSidesEngish