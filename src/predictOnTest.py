'''
Created on 02-Oct-2016

@author: harshit
'''

import pandas as pd
import numpy as np
import pickle
import operator
import mpnSimilarity

combined_data = pd.read_csv('../data/CAX_Train_Test_Combined.csv', dtype={'mpn_qs': object})

train_data_only = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

K = 5000 #clusters

lasTrainID = 53957

with open('../pickles/cluster_maps_k_5000_test_train_comb.pickle', 'rb') as f:
    clusterMaps = pickle.load(f)

with open('../pickles/train_test_comb_row_wise_filtered_content.pickle', 'rb') as f3:
    train_row_wise_filtered_content = pickle.load(f3)

counter = 0

predictions = {}

for k in range(K):
    clusterMpns = []
    valid_rows = []
    
    rows_curr_custer = clusterMaps[k]
    
    for row in rows_curr_custer:
        idd = row+1
        
        if idd <= lasTrainID:
            train_selected = train_data_only[train_data_only['id'] == idd]
            clusterMpns.extend(train_selected['mpn_qs'])
        else:
            valid_rows.append(row)
    
    print "cluster is: ", k
   
    
    for rowVal in valid_rows:
        candidateWordsTemp = []
        candidateWordsTemp.extend(train_row_wise_filtered_content[rowVal])
        
        #candidateWords = getMostProbSusbtrs(candidateWordsTemp)
        candidateWords = filter(lambda x : x is not "", candidateWordsTemp)
        
        mostProbMPN = mpnSimilarity.mostProbableMPN(candidateWords, clusterMpns)
        
        idd = rowVal+1
        predictions[idd] = mostProbMPN
        
        print "at ", counter
        counter += 1

header = "id,mpn_qs\n"

f = open('../aux_data/submission.csv','w')

sortedById = sorted(predictions.items(), key=operator.itemgetter(0))

f.write(header)
for k, v in sortedById:
    f.write(str(k) + "," + v.encode('ascii', 'ignore') + '\n')

f.close()

    
    
    
    
    

