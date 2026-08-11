class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftToRight = {")":"(", 
                       "]":"[", 
                       "}":"{"}
        for c in s:
            if c in leftToRight:
                if stack and stack[-1] == leftToRight[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False