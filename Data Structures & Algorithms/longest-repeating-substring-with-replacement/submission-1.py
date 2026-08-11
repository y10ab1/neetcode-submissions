class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 2 potinters to maintain a slideing window

        l, maxf = 0, 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k: 
            # you don't need while loop, cuz our target is to find max window 
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)