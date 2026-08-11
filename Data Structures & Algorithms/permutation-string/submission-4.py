class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # find a window in s2 which has same char count as s1
        if len(s1) > len(s2):
            return False
        
        s1cnt, s2cnt = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1cnt[ord(s1[i]) - ord('a')] += 1
            s2cnt[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1cnt[i] == s2cnt[i] else 0
        
        if matches == 26: 
            return True

        l = 0
        for r in range(len(s1), len(s2)):

            s2cnt[ord(s2[r]) - ord('a')] += 1
            s2cnt[ord(s2[l]) - ord('a')] -= 1
            l += 1

            matches = 0
            for i in range(26):
                matches += 1 if s1cnt[i] == s2cnt[i] else 0
            print(matches)

            if matches == 26:
                return True

        return False

