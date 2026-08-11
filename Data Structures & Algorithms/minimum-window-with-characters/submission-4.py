class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcnt = collections.Counter(t)
        window = defaultdict(int)
        l, ans = 0, float('inf')
        res = [0, 0]
        have, need = 0, len(tcnt)
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in tcnt and window[c] == tcnt[c]:
                have += 1

            while have == need:
                if r - l + 1 < ans:
                    ans = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in tcnt and window[s[l]] < tcnt[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if ans < float('inf') else ""
                