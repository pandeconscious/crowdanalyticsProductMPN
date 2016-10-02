'''
Created on 27-Sep-2016

@author: harshit
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import pickle



#peform clustering and then randomly select certain elements from each cluster for validation set

#vectors for title column - treat each row as a separate doc

K = 5000 #clusters

#train_data = pd.read_csv('../data/CAX_Train.csv')
train_data = pd.read_csv('../data/CAX_Train_Test_Combined.csv')

train_data_title = train_data['title'].astype(str)

#train_data_mpn = train_data['mpn_qs'].astype(str)

print len(train_data_title)

vectorizer = TfidfVectorizer(max_df=0.3,min_df=2, stop_words='english', max_features=10000, lowercase=True)

X = vectorizer.fit_transform(train_data_title)

print X.shape

km = KMeans(n_clusters=K, init='k-means++', max_iter=50, n_init=3, n_jobs = -1, verbose=True)

km.fit(X)

with open('../pickles/train_test_comb_title_X_vectors.pickle', 'wb') as f:
    pickle.dump(X, f)

with open('../pickles/train_test_comb_kmeans.pickle', 'wb') as f:
    pickle.dump(km, f)


clusterAssignments =  km.predict(X)

clusterMaps = {k: [] for k in range(K)} #contains rows for each cluster

for row in range(len(clusterAssignments)):
    clusterMaps[clusterAssignments[row]].append(row)

with open('../pickles/cluster_maps_k_5000_test_train_comb.pickle', 'wb') as fi1:
    pickle.dump(clusterMaps, fi1)

f = open('../aux_data/clustered_train_test_comb_titles.txt','w')

for k, v in clusterMaps.iteritems():
    f.write('==================== k = ' + str(k) +'=======================\n')
    for r in v:
        f.write(train_data_title[r] + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('================================================================\n')
    
    

#print clusterMaps

"""  
with open('../pickles/train_title_kmeans.pickle', 'rb') as f:
    km = pickle.load(f)
    
with open('../pickles/train_title_X_vectors.pickle', 'rb') as f:
    X = pickle.load(f)


 
clusterAssignments =  km.predict(X)

clusterMaps = {k: [] for k in range(K)} #contains rows for each cluster

for row in range(len(clusterAssignments)):
    clusterMaps[clusterAssignments[row]].append(row)

print clusterMaps
"""





"""
clusterToRowMaps = {}

for rowNum in range(len(clusterAssignments)):
    clusterToRowMaps[]
"""
#PAC102200 - Pacon Kaleidoscope Multi-Purpose Paper





