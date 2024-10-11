class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrayLen = len(nums)
        res = [1] * arrayLen
        post = 1
        pre = 1

        for i in range(arrayLen):
            res[i] = pre
            pre *= nums[i]
        for i in range(arrayLen - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res

        """
        ORIGINAL/BRUTE FORCE SOLUTION: O(n^2)

        arrayLen = len(nums)
        res = [1] * arrayLen
        
        for i in range(arrayLen):
            for s in range(arrayLen):
                if i == s:
                    continue
                res[i] *= nums[s]
        
        return res
        """