'''
Created on 01-Oct-2016

@author: harshit
'''

import pandas as pd
import numpy as np
from nltk.corpus import words
from BeautifulSoup import BeautifulSoup
import mpnSimilarity

mpnTypeChars = set(['0', '1', '2', '3', '4', '5', '6', 
                   '7', '8', '9', '-', '/', '.', '+', 
                   '_', '(', ')', '#', '=', "'", ':', '&'])

unwantedLeftChars = "-/.+_()#='&`*,:\\%$@!~^{}[]|?<>;"
unwantedRightChars = "-/.+_(#'&`*,:\\%$@!~^{}[]|?<>;"

impossibleMPNChars = "*`\\%$@!~^{}[]|?<>;"

def containsAny(seq, aset):
    """ Check whether sequence seq contains ANY of the items in aset. """
    for c in seq:
        if c in aset: return True
    return False

def trimFirstLastIfNeeded(candidateWordsTemp):
    candidateWords = []
    for w in candidateWordsTemp:
        wl = w.lstrip(unwantedLeftChars)
        wr = wl.rstrip(unwantedRightChars)
        
        #parentheses trimming
        while len(wr) > 0 and wr[-1] == ')' and '(' not in wr:
            wr = wr.rstrip(')')
        
        candidateWords.append(wr)
    return candidateWords

def hasMPNtypeSpecChar(s):
    for ch in s:
        if ch in mpnTypeChars:
            return True
    return False

def strip_html(html_text):
    soup = BeautifulSoup(html_text, convertEntities=BeautifulSoup.ALL_ENTITIES)
    html_stripped = ' '.join(soup.findAll(text=True))
    return html_stripped

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

def filterFunc(s):
    if containsAny(s, impossibleMPNChars):
        return False
    
    if s.isalpha():
        return False
    
    #left and right paren coccur in mpns
    if ('(' in  s) and (')' not in s):
        return False;
    
    if ('(' not in  s) and (')' in s):
        return False;
    
    if mpnSimilarity.RepresentsInt(s) or mpnSimilarity.RepresentsFloat(s):
        if len(s) < 5 and len(s) < 12:
            return False
    
    if hasMPNtypeSpecChar(s):
        return True
    
    all_susbtr = get_all_substrings(s)
    for sub in all_susbtr:
        if len(sub) > 2 and sub in d:
            return False
    
    return True

train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})

train_data_title =  train_data['title'].astype(str)
train_data_desc =  train_data['product_description'].astype(str)
train_data_mpn_true =  train_data['mpn_qs'].astype(str)

numRows = len(train_data_mpn_true)

train_data_mpn_predicted = pd.Series(np.chararray(numRows, itemsize = 200)).astype(str)
 

d = set(words.words())

countMPNfound = 0

filteredContentTitleDescr = []

f = open('../aux_data/train_row_wise_filtered_content.txt','w')

for row in range(numRows):
    possible_mpns = []
    
    curr_title = strip_html(train_data_title[row])
    curr_title_split_Temp = curr_title.split()
    curr_title_split = trimFirstLastIfNeeded(curr_title_split_Temp)
    
    curr_desc = strip_html(train_data_desc[row])
    curr_desc_split_Temp = curr_desc.split()
    curr_desc_split = trimFirstLastIfNeeded(curr_desc_split_Temp)
    
    curr_title_filtered = filter(lambda x: filterFunc(x.lower()), curr_title_split)
    curr_desc_filtered = filter(lambda x: filterFunc(x.lower()), curr_desc_split)
    
    
    title_union_desc = set(curr_title_filtered) | set(curr_desc_filtered)
    
    filteredContentTitleDescr.append(title_union_desc)
    
    f.write('\n' + str(title_union_desc))
    
    """
    print curr_title
    print curr_title_filtered
    
    print curr_desc
    print curr_desc_filtered
    """
    
    
    tocontinue = False
    
    for tc in curr_title_filtered:
        if train_data_mpn_true[row] in tc:
            countMPNfound += 1
            tocontinue = True
            break
    
    if tocontinue == True:
        continue
    
    for dc in curr_desc_filtered:
        if train_data_mpn_true[row] in dc:
            countMPNfound += 1
            break 
    
    
    """
    title_union_desc = set(curr_title_filtered) | set(curr_desc_filtered)
    
    possible_mpns.extend(title_union_desc)
    
    if(len(possible_mpns) > 0):
        selected = np.random.choice(possible_mpns, size = 1, replace = False)
        #Sprint selected
        train_data_mpn_predicted[row] = selected[0]
    """
    
import pickle
with open('../pickles/train_row_wise_filtered_content.pickle', 'wb') as f2:
    pickle.dump(filteredContentTitleDescr, f2)
    
    
print str(countMPNfound) + " out of " + str(numRows) 
print ((train_data_mpn_predicted == train_data_mpn_true).sum())
