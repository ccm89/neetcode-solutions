class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{':
                stack.append(c)
            elif c == '[':
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == '}' and (not stack or stack[-1] != '{'):
                return False
            elif c == ']' and (not stack or stack[-1] != '['):
                return False
            elif c == ')' and (not stack or stack[-1] != '('):
                return False
            else:
                stack.pop()
        if stack:
            return False
        else:
            return True
            