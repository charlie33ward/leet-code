class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

        # ORIGINAL SOLUTION:
        #
        # if len(s) != len(t):
        #     return False 
        # letters = {}

        # for char in s:
        #     if char in letters:
        #         letters[char] += 1
        #     else:
        #         letters[char] = 1
        # for char in t:
        #     if char in letters:
        #         letters[char] -= 1
        #         if letters[char] == 0:
        #             del letters[char]
        #     else:
        #         return False

        # return len(letters) == 0
