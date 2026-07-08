class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}

        for p in s:
            if p in d and stack and stack[-1] == d[p]:
                stack.pop()
            else:
                stack.append(p)

        if not stack:
            return True

        return False