'''
Created on 03-Oct-2016

@author: harshit
'''

f = open('../aux_data/crossOut.txt','r')

lines = f.readlines()

print len(lines)

numLines = len(lines)

i = 0

jointDistr = {}

while i < numLines:
    if "actual mpn:" in lines[i]:
        actual_mpn = lines[i].split(':')[1].strip()
        i += 1
        predicted_mpn = lines[i].split(':')[1].strip()
        
        indFound = predicted_mpn.find(actual_mpn)
        
        if indFound > -1:
            print predicted_mpn, actual_mpn
            distLeft = indFound
            endInd = indFound + len(actual_mpn) -1
            distRight = len(predicted_mpn) - 1 - endInd
            
            oldVal = jointDistr.get((distLeft, distRight))
            
            if oldVal == None:
                jointDistr[(distLeft, distRight)] = 1
            else:
                jointDistr[(distLeft, distRight)] = oldVal+1
        
    i += 1
    
f3 = open('../aux_data/crossOut_jointDistr_lef_right_distances_mpn_susbtr.txt','w')

for k, v in jointDistr.iteritems():
    f3.write("\n" + str(k) + " ==> " + str(v))