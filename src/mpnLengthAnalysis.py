'''
Created on 02-Oct-2016

@author: harshit
'''

import pandas as pd
import numpy as np
import mpnSimilarity

train_data = pd.read_csv('../data/CAX_Train.csv')

train_data_mpn = train_data['mpn_qs'].astype(str)

all_int_mpn_lengths = []

all_float_mpn_lengths = []

all_other_mpn_lengths = []

for mpn in train_data_mpn:
    
    if mpnSimilarity.RepresentsInt(mpn):
        all_int_mpn_lengths.append(len(mpn))
    elif mpnSimilarity.RepresentsFloat(mpn):
        all_float_mpn_lengths.append(len(mpn))
    else:
        all_other_mpn_lengths.append(len(mpn))

all_int_ln_np = np.array(all_int_mpn_lengths)
all_float_ln_np = np.array(all_float_mpn_lengths)
all_ohter_ln_np = np.array(all_other_mpn_lengths)

print "int total:", len(all_int_ln_np)
print "int mean:", all_int_ln_np.mean()
print "int std:", all_int_ln_np.std()
print (all_int_ln_np <= 11).sum()
print (all_int_ln_np >= 6).sum()


print '\n'

print "float total:", len(all_float_ln_np)
print "float mean:", all_float_ln_np.mean()
print "float std:", all_float_ln_np.std()
print (all_float_ln_np <= 11).sum()
print (all_float_ln_np >= 6).sum()

print '\n'

print "rest total:", len(all_ohter_ln_np)
print "rest mean:", all_ohter_ln_np.mean()
print "rest std:", all_ohter_ln_np.std()
print (all_ohter_ln_np <= 2).sum()
print (all_ohter_ln_np >= 30).sum()

