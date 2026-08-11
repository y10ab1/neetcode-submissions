class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        scnt, tcnt = [0] * 52, [0] * 52

        for i in range(len(s)):
            scnt[self.encode(s[i])] += 1
        for i in range(len(t)):
            tcnt[self.encode(t[i])] += 1

        l, r = 0, len(s) - 1
        while l < r:
            if scnt[self.encode(s[l])] - 1 >= tcnt[self.encode(s[l])]:
                scnt[self.encode(s[l])] -= 1
                l+=1
            elif scnt[self.encode(s[r])] - 1 >= tcnt[self.encode(s[r])]:
                scnt[self.encode(s[r])] -= 1
                r-=1
            else:
                break
        
        if self.cmpcode(scnt, tcnt):
            return s[l:r+1]
        return ""


    def encode(self, char):
        if char.isupper():
            return 26 + ord(char) - ord('A')
        return ord(char) - ord('a')

    def cmpcode(self, cnt1, cnt2):
        for i in range(52):
            if cnt1[i] < cnt2[i]:
                return False
        return True
