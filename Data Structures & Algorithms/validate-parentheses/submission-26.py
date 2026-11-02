class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in pairs: # close
                if len(stack) == 0 or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False