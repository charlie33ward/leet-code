class Solution:
    """
    - Grouping anagrams together: can sort all characters, anagrams will be the exact same
    - Another option: use list to identify characters and frequency, then can insert original word into hashmap value
        - hashmap key will be the list of characters/frequency
        - all anagrams will end up underneath their specific key
        - Time complexity: O(m * n)
            - m -> total number of input strings
            - n -> avg length of string
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #m mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple[count]].append(s)

        return res.values()
    
