class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set('([{')
        closing = set(')]}')
        pairs = set(['()','[]','{}'])

        for i in s:
            if i in opening:
                stack.append(i)

            if i in closing and not stack:
                return False

            if i in closing and ((stack[-1] + i) not in pairs):
                return False

            if i in closing and ((stack[-1] + i) in pairs):
                stack.pop()

        return len(stack) == 0