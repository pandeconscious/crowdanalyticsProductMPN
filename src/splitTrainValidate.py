'''
Created on 30-Sep-2016

@author: harshit
'''

import pickle
import pandas as pd
import numpy as np
from numpy import dtype


K = 5000 #clusters


"""
with open('../pickles/train_title_kmeans.pickle', 'rb') as f:
    km = pickle.load(f)
    
with open('../pickles/train_title_X_vectors.pickle', 'rb') as f:
    X = pickle.load(f)


 
clusterAssignments =  km.predict(X)

clusterMaps = {k: [] for k in range(K)} #contains rows for each cluster

for row in range(len(clusterAssignments)):
    clusterMaps[clusterAssignments[row]].append(row)

with open('../pickles/cluster_maps_k_5000.pickle', 'wb') as f:
    pickle.dump(clusterMaps, f)
"""

with open('../pickles/cluster_maps_k_5000.pickle', 'rb') as f:
    clusterMaps = pickle.load(f)

#for each cluster randomly split in 20% validate and 80 % train if size >= 5
#else don't split



train_data = pd.read_csv('../data/CAX_Train.csv')

numRows =  len(train_data)

validArr = np.zeros(numRows, dtype = bool)

for k in range(K):
    curr_cluster_size = len(clusterMaps[k])
    if(curr_cluster_size >= 5):
        valid_size = (curr_cluster_size/5) + 1
        valid_rows = np.random.choice(clusterMaps[k], size = valid_size, replace = False)
        for row in valid_rows:
            validArr[row] = True
    

trainArr = ~validArr

valid_data = train_data[validArr]

train_data = train_data[trainArr]

valid_data.to_csv('../aux_data/valid_split.csv', index = False)

train_data.to_csv('../aux_data/train_split.csv', index = False)




