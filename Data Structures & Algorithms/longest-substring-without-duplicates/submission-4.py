class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        leftmost = -1
        d = {}
        res = 0
        for i, c in enumerate(s):
            if c in d:
                leftmost = max(leftmost, d[c]) # occur duplicated char
            d[c] = i
            res = max(res, i - leftmost)
        
        return res