'''
Created on 02-Oct-2016

@author: harshit
'''

import pandas as pd
import numpy as np
import pickle
import operator
import mpnSimilarity


def getMostProbSusbtrs(candidateWordsTemp):
    candidateWords = []
    for i in jointDistrTop:
        for w in candidateWordsTemp:
            startInd = 0 + i[0][0]
            endInd = len(w) - 1 - i[0][1]
            
            if endInd >= startInd:
                candidateWords.append(w[startInd:endInd+1])
    return candidateWords



train_data = pd.read_csv('../aux_data/train_split.csv', dtype={'mpn_qs': object})
valid_data = pd.read_csv('../aux_data/valid_split.csv', dtype={'mpn_qs': object})

valid_data_mpn_true =  valid_data['mpn_qs'].astype(str)

numRows = len(valid_data_mpn_true)
valid_data_mpn_predicted = pd.Series(np.chararray(numRows, itemsize = 200)).astype(str)

K = 5000 #clusters

with open('../pickles/cluster_maps_k_5000.pickle', 'rb') as f:
    clusterMaps = pickle.load(f)

with open('../pickles/train_jointDistr_lef_right_distances_mpn_susbtr.pickle', 'rb') as f2:
    jointDistr = pickle.load(f2)

jointDistrSortedByScores = sorted(jointDistr.items(), key=operator.itemgetter(1))

jointDistrTop = filter(lambda x: x[1] > 50, jointDistrSortedByScores)

with open('../pickles/train_row_wise_filtered_content.pickle', 'rb') as f3:
    train_row_wise_filtered_content = pickle.load(f3)

counter = 0
matched = 0
for k in range(K):
    clusterMpns = []
    valid_rows = []
    
    rows_curr_custer = clusterMaps[k]
    

    
    for row in rows_curr_custer:
        idd = row+1
        train_selected = train_data[train_data['id'] == idd]
        
        if len(train_selected) == 0:#if not in train then in valid
            valid_rows.append(row)
        else:
            clusterMpns.extend(train_selected['mpn_qs'])
    
    print "cluster is: ", k
   
    
    for rowVal in valid_rows:
        candidateWordsTemp = []
        candidateWordsTemp.extend(train_row_wise_filtered_content[rowVal])
        
        #candidateWords = getMostProbSusbtrs(candidateWordsTemp)
        candidateWords = candidateWordsTemp
        
        mostProbMPN = mpnSimilarity.mostProbableMPN(candidateWords, clusterMpns)
        
        idd = rowVal+1
        rowToSet = valid_data[valid_data['id'] == idd].index.tolist()
        #print rowToSet
        valid_data_mpn_predicted[rowToSet[0]] = mostProbMPN
        print "at ", counter
        counter += 1
        
        if mostProbMPN == valid_data_mpn_true[rowToSet[0]]:
            matched += 1
        else:
            print "cluster mpns: ", clusterMpns
            print "candidate words: ", candidateWords
            print "actual mpn: ", valid_data_mpn_true[rowToSet[0]]
            print "predicted mpn: ",  mostProbMPN
        
        print "accuracy so far: ", (matched*100)/counter
        
        print "==============================================================="
        #print '\n'
        

print (((valid_data_mpn_predicted == valid_data_mpn_true).sum())*100) / numRows
    
    
    
    
    
    

