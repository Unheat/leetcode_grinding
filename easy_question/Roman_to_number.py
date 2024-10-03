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
        for first_letter, letter in zip(s, s[1:]):
            if convertTable[first_letter]<convertTable[letter]:
                sum -= convertTable[first_letter]
            else: sum += convertTable[first_letter]
        sum += convertTable[s[-1]]
        return sum
