#Scrambled message encoder
#Gaius Letters

import string

scrambled = input()
unscrambled = ""
scrambledList = list(scrambled)

for i in range (0,len(scrambledList)):
    if 97 <= ord(scrambled[i]) <= 122:
        if ord(scrambled[i]) >= 109:
            scrambledList[i] = chr(ord(scrambled[i])-12)
        else:
            scrambledList[i] = chr(ord(scrambled[i]) +14)
    elif 65 <= ord(scrambled[i]) <= 90:
        if ord(scrambled[i]) >= 77:
            scrambledList[i] = chr(ord(scrambled[i])-12)
        else:
            scrambledList[i] = chr(ord(scrambled[i]) +14)
        
scrambled = "".join(scrambledList)
print(scrambled)

    

