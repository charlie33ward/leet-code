class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        # ORIGINAL ATTEMPT: only works when all parentheses opened before any are closed
        #
        # tracker = []
        #
        # for x in range(len(s)):
        #     tracker.append(s[x])
        #     match s[x]:
        #         case '(':
        #             if (s[-x - 1] != ')'):
        #                 return False
        #         case '{':
        #             if (s[-x - 1] != '}'):
        #                 return False
        #         case '[':
        #             if (s[-x - 1] != ']'):
        #                 return False
        #         case ']':
        #             if '[' not in tracker:
        #                 return False
        #         case '}':
        #             if '{' not in tracker:
        #                 return False
        #         case ')':
        #             if '(' not in tracker:
        #                 return False
        #         case _:
        #             return False
        #
        # return True