class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Bucket sort:
        # - make a new array (of arrays) using the length of input array as the size
        # - Map values to an inner array at the index that matches their count (1 appears 3 times -> index 3)
        # - multiple values can be mapped to each index, an array of arrays
        # - scan array from top to bottom to find most common numbers

        # Alternative solution: use heapq, remove smallest item (pop from index 0) when len(heap) > k

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result
        
