'''
Created on 01-Oct-2016

@author: harshit
'''

"""
test if english words in mpn
"""

import pandas as pd
from nltk.corpus import words
import re

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]


train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

train_data_mpn = train_data['mpn_qs'].astype(str)

d = set(words.words())

f = open('../aux_data/train_english_containing_mpns.txt','w')

for mpn in train_data_mpn:
    mpn_split = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>? ]', mpn)
    for s in mpn_split:
        if len(s) > 3 and s.lower() in d:
            f.write(s + "==>" +  mpn + "\n")
            break
            
"""
for mpn in train_data_mpn:
    mpn_split = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', mpn)
    for s in mpn_split:
        if len(s) > 0 and d.check(s) and re.match("\W+", s):
            print mpn
            break
"""
    

