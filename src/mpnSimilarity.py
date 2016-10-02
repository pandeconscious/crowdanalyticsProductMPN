'''
Created on 01-Oct-2016

@author: harshit
'''

import operator

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def scoreMPN(candidateWord, clusterMpns):
    score = 0;
    lenCand = len(candidateWord)
    
    firstCand = ""
    firstTwoCand = ""
    firstThreeCand = ""
    lastCand = ""
    lastTwoCand = ""
    lastThreeCand = ""
    
    if lenCand > 0:
        firstCand = candidateWord[0]
        lastCand = candidateWord[-1]
    
    if lenCand > 1:
        firstTwoCand = candidateWord[0:2]
        lastTwoCand = candidateWord[-2:]
        
    if lenCand > 2:
        firstThreeCand = candidateWord[0:3]
        lastThreeCand = candidateWord[-3:]
    
    candIsInt = RepresentsInt(candidateWord)
    candIsFloat = False
    
    if candIsInt == False:
        candIsFloat = RepresentsFloat(candidateWord)
    
    
    
    candContainsHyphen = '-' in candidateWord
    candContainsSlash = '/' in candidateWord
    candConstainsDot = '.' in candidateWord
    candContainsPlus = '+' in candidateWord
    candContainsUnderScore = '_' in candidateWord
    candConstainsLeftParen = '(' in candidateWord
    candContainsRightParen = ')' in candidateWord
    candContainsHash = '#' in candidateWord
    candContainsEqual = '=' in candidateWord
    candContainsQuote = "'" in candidateWord
    candContainsColon = ':' in candidateWord
    candContainsApersand = '&' in candidateWord
    
    
    for clustMPN in clusterMpns:
        
        lenClustMPN = len(clustMPN)
        lenDiff = abs(lenClustMPN - lenCand)
        
        if lenDiff == 0:
            score += 4
        elif lenDiff == 1:
            score += 2
        elif lenDiff == 2:
            score += 1
        
        clustMPNIsInt = RepresentsInt(clustMPN) 
        
        clustMPNIsFloat = False
        
        if clustMPNIsInt == False:
            clustMPNIsFloat = RepresentsFloat(clustMPN)
        
        if clustMPNIsInt == True and candIsInt == True:
            score += 4
        elif clustMPNIsFloat == True and candIsFloat == True:
            score += 4
        
        firstClustMPN = ""
        firstTwoClustMPN = ""
        firstThreeClustMPN = ""
        lastClustMPN = ""
        lastTwoClustMPN = ""
        lastThreeClustMPN = ""
            
        if lenClustMPN > 0:
            firstClustMPN = clustMPN[0]
            lastClustMPN = clustMPN[-1]
                
            if firstCand == firstClustMPN:
                score += 2
                    
            if lastCand == lastClustMPN:
                score += 2
        
            
        if lenClustMPN > 1:
            firstTwoClustMPN = clustMPN[0:2]
            lastTwoClustMPN = clustMPN[-2:]
                
            if firstTwoCand == firstTwoClustMPN:
                score += 4
                    
            if lastTwoCand == lastTwoClustMPN:
                score += 4
                
        if lenClustMPN > 2:
            firstThreeClustMPN = clustMPN[0:3]
            lastThreeClustMPN = clustMPN[-3:]
                
            if firstThreeCand == firstThreeClustMPN:
                score += 6
                    
            if lastThreeCand == lastThreeClustMPN:
                score += 6
            
        clustMPNContainsHyphen = '-' in clustMPN
        clustMPNContainsSlash = '/' in clustMPN
        clustMPNConstainsDot = '.' in clustMPN
        clustMPNContainsPlus = '+' in clustMPN
        clustMPNContainsUnderScore = '_' in clustMPN
        clustMPNConstainsLeftParen = '(' in clustMPN
        clustMPNContainsRightParen = ')' in clustMPN
        clustMPNContainsHash = '#' in clustMPN
        clustMPNContainsEqual = '=' in clustMPN
        clustMPNContainsQuote = "'" in clustMPN
        clustMPNContainsColon = ':' in clustMPN
        clustMPNContainsApersand = '&' in clustMPN
        
        if clustMPNContainsHyphen == True and candContainsHyphen == True:
            score += 2
        
        if clustMPNContainsSlash == True and candContainsSlash == True:
            score += 1
            
        if clustMPNConstainsDot == True and candConstainsDot == True:
            score += 0.8
        
        if clustMPNContainsPlus == True and candContainsPlus == True:
            score += 0.6
        
        if clustMPNContainsUnderScore == True and candContainsUnderScore == True:
            score += 0.5
        
        if clustMPNConstainsLeftParen == True and candConstainsLeftParen == True and clustMPNContainsRightParen == True and candContainsRightParen == True:
            score += 0.5
        
        if clustMPNContainsHash == True and candContainsHash == True:
            score += 0.4
            
        if clustMPNContainsEqual == True and candContainsEqual == True:
            score += 0.3
        
        if clustMPNContainsQuote == True and candContainsQuote == True:
            score + 0.2
        
        if clustMPNContainsColon == True and candContainsColon == True:
            score += 0.2
            
        if clustMPNContainsApersand == True and candContainsApersand  == True:
            score += 0.2
        
    
    return score;

def mostProbableMPN(candidateWords, clusterMpns):
    rankedCands = {}
    
    if candidateWords is None or clusterMpns is None:
        return ""
    
    if len(candidateWords) == 0 or len(clusterMpns) == 0:
        return ""
    
    for candWord in candidateWords:
        score = scoreMPN(candWord, clusterMpns)
        rankedCands[candWord] = score
    
    sortedByScores = sorted(rankedCands.items(), key=operator.itemgetter(1))
    
    return sortedByScores[-1][0]


if __name__ == '__main__':
    candidateWords = [u'der-mounted', u'MHSN6636A01', '1b-cd-89']
    clusterMpns = ['MHCO6030C01', 'MHCO6036A04', 'MHCO6036C02', 'MHCO7236C04', 'MHDE6042A08', 'MHSN6636A03', 'MHVN6030A01']
    
    print mostProbableMPN(candidateWords, clusterMpns)
    
    
    