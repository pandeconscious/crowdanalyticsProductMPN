'''
Created on 30-Sep-2016

@author: harshit
'''

import pandas as pd
from collections import defaultdict

train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

train_data_title = train_data['title'].astype(str)
train_data_desc = train_data['product_description'].astype(str)
train_data_mpn = train_data['mpn_qs'].astype(str)

numRows = len(train_data)

f = open('../aux_data/train_mismatch_rows_substr_based.txt','w')

misMatchCount = 0

#a map from a tuple of 2 ints to int
#distr to store the counts for 
#(substr startind distance from left, susbtr endind distance from right)

jointDistr = {}

jointDistrRows = defaultdict(list) 


for i in range(numRows):
    title_split = train_data_title[i].split()
    desc_split = train_data_desc[i].split()
    
    found = False
    
    for tc in title_split:
        indFound = tc.find(train_data_mpn[i])
        if indFound > -1:
            found = True
            
            distLeft = indFound
            endInd = indFound + len(train_data_mpn[i]) -1
            distRight = len(tc) - 1 - endInd
            
            oldVal = jointDistr.get((distLeft, distRight))
            
            if oldVal == None:
                jointDistr[(distLeft, distRight)] = 1
            else:
                jointDistr[(distLeft, distRight)] = oldVal+1
                
            jointDistrRows[(distLeft, distRight)].append(i)
            
            
            break
    
    if found == False:  
        for dc in desc_split:
            indFound = indFound = dc.find(train_data_mpn[i])
            if indFound > -1:
                found = True
                
                distLeft = indFound
                endInd = indFound + len(train_data_mpn[i]) - 1
                distRight = len(dc) - 1 - endInd
                
                oldVal = jointDistr.get((distLeft, distRight))
                
                if oldVal == None:
                    jointDistr[(distLeft, distRight)] = 1
                else:
                    jointDistr[(distLeft, distRight)] = oldVal+1
                
                jointDistrRows[(distLeft, distRight)].append(i)
                
                break
        
    
    if found == False:
        misMatchCount += 1
        f.write( "\nrow with id " + str(i+ 1) + " couldn't find substring-based overlap")

f.write("\nTotal mismatched: " + str(misMatchCount) + " out of " + str(numRows))


import pickle
with open('../pickles/train_jointDistr_lef_right_distances_mpn_susbtr.pickle', 'wb') as f2:
    pickle.dump(jointDistr, f2)


f3 = open('../aux_data/train_jointDistr_lef_right_distances_mpn_susbtr.txt','w')

for k, v in jointDistr.iteritems():
    f3.write("\n" + str(k) + " ==> " + str(v))
    
f4 = open('../aux_data/train_joint_left_right_rows_list_substr_based.txt','w')
for k, v in jointDistrRows.iteritems():
    f4.write("\n" + str(k) + " ==> " + str(v))

    
