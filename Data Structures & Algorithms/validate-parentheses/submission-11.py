class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in {')', ']', '}'} and not stack:
                return False
            elif p in {'(', '[', '{'}:
                stack.append(p)
            elif stack[-1] == '(' and p == ')':
                stack.pop()
            elif stack[-1] == '[' and p == ']':
                stack.pop()
            elif stack[-1] == '{' and p == '}':
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True

            


            
            
