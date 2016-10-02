'''
Created on 02-Oct-2016

@author: harshit
'''

import re
import pandas as pd


patternSize = re.compile("^[0-9]+\-[1-9]/[1-9]$")

patternUnit = re.compile("^[0-9]{1,2}\s*[a-zA-Z]{2}$")

train_data = pd.read_csv('../data/CAX_Train.csv')
train_data_mpn = train_data['mpn_qs'].astype(str)
train_data_desc = train_data['product_description'].astype(str)


counterSizeMPN = 0
counterSizeDESC = 0

counterUnitMPN = 0
counterUnitDESC = 0


for mpn in train_data_mpn:
    if patternSize.match(mpn):
        counterSizeMPN += 1
    
    if patternUnit.match(mpn):
        counterUnitMPN += 1

for desc in train_data_desc:
    desc_split = desc.split()
    for d in desc_split:
        if patternSize.match(d):
            counterSizeDESC += 1
        
        if patternUnit.match(d):
            print d
            counterUnitDESC += 1


print "size pattern found ", counterSizeMPN, " times in mpns"
print "size pattern found ", counterSizeDESC, " times in description"

print "unit pattern found ", counterUnitMPN, " times in mpns"
print "unit pattern found ", counterUnitDESC, " times in description"