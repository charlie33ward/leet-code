class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
        
        
        """
        ORIGINAL SOLUTION: invalid, runs in o(nlogn)

        if not nums:
            return 0
        
        sortedList = sorted(set(nums))
        prev = sortedList[0]
        res = 1
        sequenceCounter = 1

        for i in range(1, len(sortedList)):
            if sortedList[i] == (prev + 1):
                sequenceCounter += 1
            else:
                sequenceCounter = 1

            res = max(sequenceCounter, res)
            prev = sortedList[i]
        
        return res"""