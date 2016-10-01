'''
Created on 30-Sep-2016

@author: harshit
'''

import pandas as pd

train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

train_data_title = train_data['title'].astype(str)
train_data_desc = train_data['product_description'].astype(str)
train_data_mpn = train_data['mpn_qs'].astype(str)

numRows = len(train_data)

f = open('../aux_data/train_mismatch_rows_naive.txt','w')

misMatchCount = 0

for i in range(numRows):
    title_split = train_data_title[i].split()
    desc_split = train_data_desc[i].split()
    
    found = False
    
    for tc in title_split:
        if train_data_mpn[i] == tc:
            found = True
            break
    
    if found == False:  
        for dc in desc_split:
            if train_data_mpn[i] == dc:
                found = True
                break
        
    if found == False:
        misMatchCount += 1
        f.write( "\nrow with id " + str(i+ 1) + " couldn't find overlap")

f.write("\nTotal mismatched: " + str(misMatchCount) + " out of " + str(numRows))
    
