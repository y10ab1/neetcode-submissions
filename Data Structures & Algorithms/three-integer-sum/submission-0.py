class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each element in nums, it is a 2 sum problem
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            s = set()
            for j in range(i+1, len(nums)):
                if nums[j] in s:
                    res.add(tuple(sorted([-target, target-nums[j], nums[j]])))
                else:
                    s.add(target - nums[j])
        
        return [list(t) for t in res]