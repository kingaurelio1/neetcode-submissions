class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = '{}()[]'
        pairs = { '(':')', '{':'}', '[':']'}
        stack = []

        for i in s:
            if i in pairs:
                stack.append(i)

            else:
                if not stack or stack[-1] + i not in is_valid:
                    return False

                else:
                    stack.pop()


        return len(stack) == 0

        