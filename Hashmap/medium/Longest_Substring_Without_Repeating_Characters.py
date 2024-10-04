'''https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=hash-table'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 0

        # existedTable = {}
        # total = 0
        # for letter in s:
        #     if letter in existedTable:
        #         pass
        #     else: 
        #         existedTable[letter] = 'exist'
        #         total += 1
        # return total
#upper code is wrong because it depict subsequence not substring, substring must be các chứ liền nhau trong string
        existedTable = {}
        total = 0
        temp = 0
        for letter in s:
            if letter in existedTable:
                if total > temp:
                    temp = total # temp để lưu trữ substring lớn nhất trước pointer
                existedTable = {}
                total = 1 #start again
                existedTable[letter] = 'exist'
                
            else: 
                existedTable[letter] = 'exist'
                total += 1

        return temp

