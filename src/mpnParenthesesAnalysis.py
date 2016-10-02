'''
Created on 02-Oct-2016

@author: harshit
'''
import pandas as pd

train_data = pd.read_csv('../data/CAX_Train.csv')

train_data_mpn = train_data['mpn_qs'].astype(str)

train_data_mpn_right_paren = train_data_mpn[train_data_mpn.str.contains("\)")]

lef_paren_inds = set(train_data_mpn_right_paren.index.tolist())

train_data_mpn_left_paren = train_data_mpn[train_data_mpn.str.contains("\(")]

right_paren_inds = set(train_data_mpn_left_paren.index.tolist())

print len(lef_paren_inds & right_paren_inds)
