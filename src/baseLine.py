'''
Created on 30-Sep-2016

@author: harshit
'''

import pandas as pd
import numpy as np
from nltk.corpus import words

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

def noEngish(s):
    all_susbtr = get_all_substrings(s)
    for sub in all_susbtr:
        if len(sub) > 2 and sub in d:
            return False
    
    return True

#train_data = pd.read_csv('../aux_data/train_split.csv', dtype={'mpn_qs': object})
valid_data = pd.read_csv('../aux_data/valid_split.csv', dtype={'mpn_qs': object})

valid_data_title =  valid_data['title'].astype(str)
valid_data_desc =  valid_data['product_description'].astype(str)
valid_data_mpn_true =  valid_data['mpn_qs'].astype(str)

numRows = len(valid_data_mpn_true)

valid_data_mpn_predicted = pd.Series(np.chararray(numRows, itemsize = 200)).astype(str)
 

d = set(words.words())


for row in range(numRows):
    possible_mpns = []
    
    curr_title = valid_data_title[row]
    curr_title_split = curr_title.split()
    
    for s in curr_title_split:
        if noEngish(s.lower()):
            possible_mpns.append(s)
        
    
    curr_desc = valid_data_desc[row]
    curr_desc_split = curr_desc.split()
    
    for s in curr_desc_split:
         if noEngish(s.lower()):
            possible_mpns.append(s)
    
    #randomly select one mpn
    #Sprint possible_mpns
    
    if(len(possible_mpns) > 0):
        selected = np.random.choice(possible_mpns, size = 1, replace = False)
        #Sprint selected
        valid_data_mpn_predicted[row] = selected[0]
    
        
    #Sprint "==================================================="

    


print ((valid_data_mpn_predicted == valid_data_mpn_true).sum())



#train_data_mpn = train_data['mpn_qs'].astype(str)