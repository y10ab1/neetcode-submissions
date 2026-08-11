class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s, f = nums[s], nums[nums[f]]
            if s == f: break
        t = 0
        while True:
            s, t = nums[s], nums[t]
            if s == t: break
        return t
