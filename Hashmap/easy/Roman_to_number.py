class Solution:
    def romanToInt(self, s: str) -> int:
        convertTable = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = 0
        for first_letter, letter in zip(s, s[1:]):  #s is the first list and s[1:] is the secind list 
            if convertTable[first_letter]<convertTable[letter]:
                sum -= convertTable[first_letter]
            else: sum += convertTable[first_letter]
        sum += convertTable[s[-1]]
        return sum


'''
zip is the key here as it allow us to check 2 letter at the same time when loop through the string
to use zip: zip(list1,list2,list3,...) it will connect first index of list1 with list2, list3,...then second index,....
to loop through zip() we should create equal number of loop variable (ex:first_letter, letter) to the number of list or we can only 
crete 1-this will make that loop var become the entire merged value from different lists (1 or equal)
'''



