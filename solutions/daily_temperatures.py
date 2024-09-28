class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate over stack once, using monotonic stack to insert items in output list
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append([t, i])
        return output
        