'''
Created on 01-Oct-2016

@author: harshit
'''

import pandas as pd
import numpy as np
from nltk.corpus import words
from nltk.corpus import gutenberg
from BeautifulSoup import BeautifulSoup
import mpnSimilarity
import re

mpnTypeChars = set(['0', '1', '2', '3', '4', '5', '6', 
                   '7', '8', '9', '-', '/', '.', '+', 
                   '_', '(', ')', '#', '=', "'", ':', '&'])

unwantedLeftChars = "-/.+_()#='&`*,:\\%$@!~^{}[]|?<>;"
unwantedRightChars = "-/.+_(#'&`*,:\\%$@!~^{}[]|?<>;"

impossibleMPNChars = "*`\\%$@!~^{}[]|?<>,;"

splitChars = "[\s,;|]"

patternSize = re.compile("^[0-9]+\-[1-9]/[1-9]$")

patternUnit = re.compile("^[0-9]{1,2}\s*[a-zA-Z]{2}$")

patternVolts = re.compile("^[0-9]{1,4}[Vv]$")

"""
if title contains Classic Lighting - pattern between 
"""
classicLightTitlePatternLong = re.compile("\s[0-9]{4,5}\s+[A-Z]{1,3}\s+[A-Z]{1,3}\s")
classicLightTitlePatternShort = re.compile("\s[0-9]{4,5}\s+[A-Z]{1,3}\s")

"""
if title contains Chicago Hardware - pattern between
"""
chicagoHardwarePattern = re.compile("[\s(][0-9]{5}\s+[0-9][\s)]")

"""
if title contains CK Series - pattern no between
"""
CKSeriesPattern = re.compile("[C][K]\s+[0-9]{3,4}\s+[A-Z]{1,2}")


"""
if title contains BP Series - pattern no between
"""
BPSeriesPattern = re.compile("[B][P]\s+[0-9]{3,4}\s+[A-Z]{2}")

"""
if title contains CF Series - pattern no between
"""
CFSeriesPattern = re.compile("[C][F]\s+[0-9]{3,4}\s+[A-Z]{1,2}")

"""
if title contains CP Series - pattern no between
"""
CPSeriesPattern = re.compile("^[C][P]\s+[0-9]{2,4}\s+[A-Z]{1,2}")

"""
if title contains Transglobe or Trans Globe,  - pattern between
"""
transGlobePattern = re.compile("\s[0-9]{4,5}\s+[A-Z]{2,3}\s")

"""
if title contains Legris  - pattern between
"""
legrisGlobePattern = re.compile("\s[0-9]{4}\s+[0-9]{2}\s+[0-9]{2}\s")

"""
if title contains PLC Lighting  - pattern between
"""
plcLighGlobePattern = re.compile("\s[0-9]{3,5}\s+[A-Z]{2}\s")


"""
if title contains Drawer .* Finish - pattern no between
"""
drawerSeriesPattern = re.compile("^.*[L][o][c][k]\)")

"""
if title contains Egyptian Cotton - pattern no between
"""
egyptianCottonPattern = re.compile("^[0-9]{3,4}[A-Z]{4}\s+[A-Z]{4}")

"""
if title contains KNIPEX or Knipex  - pattern between
"""
knipexPattern = re.compile("\s[0-9]{2}\s+[0-9]{2}\s+[0-9A-Z]{2,3}\s")

"""
if title contains Sandvik Coromant - pattern between
"""
sandvikPattern = re.compile("\s[0-9]{3}[\.][1][\-][0-9]{4}[\-].{5}[\-][A-Z]{2}\s+[0-9A-Z]{4}\s")

"""
if title contains Commercial Edition  - pattern no between
"""
commercialEditionPattern = re.compile("^[C][F][S][L].{1,18}[\)]{1}")

"""
if title contains Mario Pressure  - pattern no between
"""
marioPressurePattern = re.compile("^[R][e][m][e][r]\s+.{6}")

"""
if title contains Peleo Pressure or Tyga Pressure  or Galiano Pressure- pattern no between
"""
peleoPressurePattern = re.compile("^[R][e][m][e][r]\s+.{7}")


"""
if title contains Closed Board or Open Board or Louvered Shutter or Raised Panel Shutter - pattern no between
"""
closedBoardPattern = re.compile("^[V][I][N][0-9A-Z]{6}\s+[0-9A-Z]{2}")

"""
if title contains La Cuisine- pattern between
"""
laCuisinePattern = re.compile("\s[L][C]\s+[0-9]{4}\s")


def spacedMPNsFetching(title, desc):
    if title is None:
        title = desc
    if desc is None:
        desc = title
    
    if "Classic Lighting" in title:
        mpn = getMPNFromPatternBetween(classicLightTitlePatternLong, title)
        if mpn != "":
            return mpn
        else:
            mpn = getMPNFromPatternBetween(classicLightTitlePatternShort, title)
            if mpn != "":
                return mpn
        
        mpn = getMPNFromPatternBetween(classicLightTitlePatternLong, desc)
        if mpn != "":
            return mpn
        else:
            mpn = getMPNFromPatternBetween(classicLightTitlePatternShort, desc)
            if mpn != "":
                return mpn
    
    
    if "Chicago Hardware" in title:
        mpn = getMPNFromPatternBetween(chicagoHardwarePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(chicagoHardwarePattern, desc)
        if mpn != "":
            return mpn
    
    if "Transglobe" in title or "Trans Globe" in title:
        mpn = getMPNFromPatternBetween(transGlobePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(transGlobePattern, desc)
        if mpn != "":
            return mpn
    
    if "Legris" in title:
        mpn = getMPNFromPatternBetween(legrisGlobePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(legrisGlobePattern, desc)
        if mpn != "":
            return mpn
    
    if "PLC Lighting" in title:
        mpn = getMPNFromPatternBetween(plcLighGlobePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(plcLighGlobePattern, desc)
        if mpn != "":
            return mpn
    
    if "KNIPEX" in title or "Knipex" in title:
        mpn = getMPNFromPatternBetween(knipexPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(knipexPattern, desc)
        if mpn != "":
            return mpn
     
    if "La Cuisine" in title:
        mpn = getMPNFromPatternBetween(laCuisinePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(laCuisinePattern, desc)
        if mpn != "":
            return mpn    
        
        
    if "Sandvik Coromant" in title:
        mpn = getMPNFromPatternBetween(sandvikPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPatternBetween(sandvikPattern, desc)
        if mpn != "":
            return mpn
        
    if "CK Series" in title:
        mpn = getMPNFromPattern(CKSeriesPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(CKSeriesPattern, desc)
        if mpn != "":
            return mpn
        
    if "BP Series" in title:
        mpn = getMPNFromPattern(BPSeriesPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(BPSeriesPattern, desc)
        if mpn != "":
            return mpn
    
    if "CF Series" in title:
        mpn = getMPNFromPattern(CFSeriesPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(CFSeriesPattern, desc)
        if mpn != "":
            return mpn
        
    if "CP Series" in title:
        mpn = getMPNFromPattern(CPSeriesPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(CPSeriesPattern, desc)
        if mpn != "":
            return mpn
        
    if re.match("Drawer .* Finish", title) is not None:
        mpn = getMPNFromPattern(drawerSeriesPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(drawerSeriesPattern, desc)
        if mpn != "":
            return mpn
    
    if "Egyptian Cotton" in title:
        mpn = getMPNFromPattern(egyptianCottonPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(egyptianCottonPattern, desc)
        if mpn != "":
            return mpn
        
    if "Commercial Edition" in title:
        mpn = getMPNFromPattern(commercialEditionPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(commercialEditionPattern, desc)
        if mpn != "":
            return mpn
        
    if "Mario Pressure" in title:
        mpn = getMPNFromPattern(marioPressurePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(marioPressurePattern, desc)
        if mpn != "":
            return mpn
    
    if "Peleo Pressure" in title or "Tyga Pressure" in title  or "Galiano Pressure" in title:
        mpn = getMPNFromPattern(peleoPressurePattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(peleoPressurePattern, desc)
        if mpn != "":
            return mpn    
    
    if "Closed Board" in title or "Open Board" in title  or "Louvered Shutter" in title or "Raised Panel Shutter" in title:
        mpn = getMPNFromPattern(closedBoardPattern, title)
        if mpn != "":
            return mpn
        
        mpn = getMPNFromPattern(closedBoardPattern, desc)
        if mpn != "":
            return mpn
    
    
    #on no found return ""
    return ""

def getMPNFromPatternBetween(mpnPattern, s):
    m = mpnPattern.search(s)
    if m is not None:
        return s[m.span()[0]+1:m.span()[1]-1]
    else:
        return ""

def getMPNFromPattern(mpnPattern, s):
    m = mpnPattern.search(s)
    if m is not None:
        return s[m.span()[0]:m.span()[1]]
    else:
        return ""

def containsAny(seq, aset):
    """ Check whether sequence seq contains ANY of the items in aset. """
    for c in seq:
        if c in aset: return True
    return False

def trimProcessing(candidateWordsTemp):
    candidateWords = []
    for w in candidateWordsTemp:
        wl = w.lstrip(unwantedLeftChars)
        wr = wl.rstrip(unwantedRightChars)
        
        #parentheses trimming
        while len(wr) > 0 and wr[-1] == ')' and '(' not in wr:
            wr = wr.rstrip(')')
        
        if mpnSimilarity.RepresentsInt(wr):
            wr = wr.lstrip('0')
            if len(wr) >= 12:
                wrnum = int(wr)
                wr = formatLongNum(wrnum)
        
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

def formatLongNum(num):
    return str("{:.2e}".format(num)).replace('e', 'E')

def filterFunc(s, secondStage = False):
    if s.strip() == "":
        return False
    
    if len(s) == 1:
        return False
    
    if '"' in s:
        return False
    
    if s[-1] == ".":
        return False
    
    if s in d or s in dgtn:
        return False
    
    if ".com" in s or ".org" in s:
        return False
    
    if ".br" in s:
        return False
    
    if "volt" in s or "Volt" in s or "VOLT" in s:
        return False
    
    if "inch" in s or "Inch" in s or "INCH" in s:
        return False
    
    if "mid" in s or "MID" in s:
        return False
    
    if "(s)" in s or "(S)" in s:
        return False
    
    if "'s" in s or "'S" in s:
        return False
    
    if "--" in s or "::" in s:
        return False
    
    if "(TM)" in s or "(R)" in s:
        return False
    
    if ".-" in s:
        return False
    
    if "watt" in s or "Watt" in s or "WATT" in s:
        return False
    
    if "type" in s or "Type" in s or "TYPE" in s:
        return False
    
    if "theme" in s or "Theme" in s or "THEME" in s:
        return False
    
    if "date" in s.lower():
        return False
    
    if "quart" in s.lower():
        return False
    
    if "style" in s.lower():
        return False
    
    if "year" in s.lower():
        return False
    
    if "month" in s.lower() or "percent" in s.lower():
        return False
    
    if patternSize.match(s):
        return False
    
    if patternUnit.match(s):
        return False
    
    if patternVolts.match(s):
        return False;
    
    if containsAny(s, impossibleMPNChars):
        return False
    
    if secondStage == False:
        if s.isalpha():
            return False
    
    #left and right paren coccur in mpns
    if ('(' in  s) and (')' not in s):
        return False;
    
    if ('(' not in  s) and (')' in s):
        return False;
    
    
    if mpnSimilarity.RepresentsInt(s) or mpnSimilarity.RepresentsFloat(s):
        if len(s) <= 5 or len(s) >= 12:
            return False
    
    
    #single hyphen, dot, slash english words filtering
    
    if secondStage == False:
        countHyphen = s.count('-')
        if countHyphen == 1:
            left, right = s.split('-')
            if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
                return False
        
        if countHyphen == 2:
            left, mid, right = s.split('-')
            if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid.lower() in d or mid.lower() in dgtn or mid in d or mid in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
                return False
            
        if countHyphen == 3:
            left, mid1,  mid2, right = s.split('-')
            if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid1.lower() in d or mid1.lower() in dgtn or mid1 in d or mid1 in dgtn) and (mid2.lower() in d or mid2.lower() in dgtn or mid2 in d or mid2 in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
                return False
        
    countDot = s.count('.')
    if countDot == 1:
        left, right = s.split('.')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
    
    countSlash = s.count('/')
    if countSlash == 1:
        left, right = s.split('/')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
        
    if countSlash == 2:
        left, mid, right = s.split('/')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid.lower() in d or mid.lower() in dgtn or mid in d or mid in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
        
    if countSlash == 3:
        left, mid1,  mid2, right = s.split('/')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid1.lower() in d or mid1.lower() in dgtn or mid1 in d or mid1 in dgtn) and (mid2.lower() in d or mid2.lower() in dgtn or mid2 in d or mid2 in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
    
    countSingleQuote = s.count("'")
    if countSingleQuote == 1:
        left, right = s.split("'")
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
        
    countColon = s.count(':')
    if countColon == 1:
        left, right = s.split(':')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
        
    if countColon == 2:
        left, mid, right = s.split(':')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid.lower() in d or mid.lower() in dgtn or mid in d or mid in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
    
    countUnd = s.count('_')
    if countUnd == 1:
        left, right = s.split('_')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
    
    if countUnd == 2:
        left, mid, right = s.split('_')
        if (left.lower() in d or left.lower() in dgtn or left in d or left in dgtn) and (mid.lower() in d or mid.lower() in dgtn or mid in d or mid in dgtn) and (right.lower() in d or right.lower() in dgtn or right in d or right in dgtn):
            return False
    
    if hasMPNtypeSpecChar(s):
        return True
    
    if secondStage == True:
        countUpperCase = 0
        for ch in s:
            if ch.isupper():
                countUpperCase += 1
        
        if countUpperCase >= 2:
            return True
    
    all_susbtr = get_all_substrings(s)
    for sub in all_susbtr:
        if secondStage == False:
            if len(sub) > 2 and (sub in d or sub in dgtn):
                return False
        else:
            if len(sub) > 3 and (sub in d or sub in dgtn):
                return False
        
    return True

#train_data = pd.read_csv('../data/CAX_Train.csv', dtype={'mpn_qs': object})
train_data = pd.read_csv('../data/CAX_Train_Test_Combined.csv', dtype={'mpn_qs': object})

train_data_title =  train_data['title'].astype(str)
train_data_desc =  train_data['product_description'].astype(str)

#train_data_mpn_true =  train_data['mpn_qs'].astype(str)

numRows = len(train_data)

#train_data_mpn_predicted = pd.Series(np.chararray(numRows, itemsize = 200)).astype(str)
 

d = set(words.words())
dgtn = set(gutenberg.words())

f = open('../data/domainSpecificDict.txt', 'r')

dd = map(lambda x: x.rstrip('\n'), f.readlines())

for ddword in dd:
    d.add(ddword)

#countMPNfound = 0

filteredContentTitleDescr = []

f = open('../aux_data/train_test_comb_row_wise_filtered_content.txt','w')
#f = open('../aux_data/train_row_wise_filtered_content.txt','w')

#femp = open('../aux_data/train_empty_candidate_words.txt','w')
femp = open('../aux_data/train_test_comb_empty_candidate_words.txt','w')

for row in range(numRows):
    possible_mpns = []
    
    curr_title = strip_html(train_data_title[row])
    curr_desc = strip_html(train_data_desc[row])
    
    title_union_desc = None
    
    spacedMPN = spacedMPNsFetching(curr_title, curr_desc)
    
    if spacedMPN != "": 
        title_union_desc = set([spacedMPN])
        
    else:    
        curr_title_split_Temp = curr_title.split()
        #curr_title_split_Temp = filter(None, re.split(splitChars, curr_title))
        curr_title_split = trimProcessing(curr_title_split_Temp)
        
        
        curr_desc_split_Temp = curr_desc.split()
        #curr_desc_split_Temp = filter(None, re.split(splitChars, curr_desc))
        curr_desc_split = trimProcessing(curr_desc_split_Temp)
        
        curr_title_filtered = filter(lambda x: filterFunc(x.lower()), curr_title_split)
        curr_desc_filtered = filter(lambda x: filterFunc(x.lower()), curr_desc_split)
        
        
        set_curr_title_filtered = set(curr_title_filtered)
        set_curr_desc_filtered = set(curr_desc_filtered)
        
        title_union_desc = set_curr_title_filtered | set_curr_desc_filtered
    
        if len(title_union_desc) == 0:
            
            
            
            curr_title_filtered = filter(lambda x: filterFunc(x.lower(), secondStage = True), curr_title_split)
            curr_desc_filtered = filter(lambda x: filterFunc(x.lower(), secondStage = True), curr_desc_split)
        
            set_curr_title_filtered = set(curr_title_filtered)
            set_curr_desc_filtered = set(curr_desc_filtered)
        
            title_union_desc = set_curr_title_filtered | set_curr_desc_filtered
            
            
        
    
    if len(title_union_desc) == 0:
        title_union_desc = set(['None'])
        print "still empty :("
        femp.write(train_data_title[row])
        femp.write('\n')
        femp.write(train_data_desc[row])
        femp.write('\n')
        #femp.write(train_data_mpn_true[row])
        femp.write('\n')
        femp.write('=================================================================\n')
    
    filteredContentTitleDescr.append(title_union_desc)
    
    f.write('\n' + str(title_union_desc))
    
    """
    print curr_title
    print curr_title_filtered
    
    print curr_desc
    print curr_desc_filtered
    """
    
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
    
    """
    title_union_desc = set(curr_title_filtered) | set(curr_desc_filtered)
    
    possible_mpns.extend(title_union_desc)
    
    if(len(possible_mpns) > 0):
        selected = np.random.choice(possible_mpns, size = 1, replace = False)
        #Sprint selected
        train_data_mpn_predicted[row] = selected[0]
    """
    
import pickle

with open('../pickles/train_test_comb_row_wise_filtered_content.pickle', 'wb') as f2:
    pickle.dump(filteredContentTitleDescr, f2)

#with open('../pickles/train_row_wise_filtered_content.pickle', 'wb') as f2:
#    pickle.dump(filteredContentTitleDescr, f2) 
   
    
#print str(countMPNfound) + " out of " + str(numRows) 
#print ((train_data_mpn_predicted == train_data_mpn_true).sum())



