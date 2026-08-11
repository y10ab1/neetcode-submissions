class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # find a window in s2 which has same char count as s1
        s1_cnt = collections.Counter(s1)
        s2_cnt = defaultdict(int)
        l = 0
        ans = False
        for r in range(len(s2)):
            s2_cnt[s2[r]] += 1
            
            if r - l + 1 == len(s1):
                ans = self.cmpdict(s1_cnt, s2_cnt)
                print(ans)
                if ans:
                    return True
                else:
                    s2_cnt[s2[l]] -= 1
                    l += 1
        return ans
                
    def cmpdict(self, d1, d2):
        for k, v in d1.items():
            if d2[k] != v:
                return False
        return True
