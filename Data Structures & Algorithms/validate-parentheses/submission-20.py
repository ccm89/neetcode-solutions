class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # track the opening brackets
        par_dict = {')': '(', '}': '{', ']':'['} # map closing brackets to propper opening brackets
        for c in s:
            # 1. Is p a valid input
            if c in par_dict: # checks keys only!
                # 2. Stack is not empty and the top is the correct match
                if stack and stack[-1] == par_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # If the stack is empty then we got all matches
        # else the stack contains a unmatched brackets
        if not stack:
            return True
        else:
            return False
