class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_nums = {}
        for idx, val in enumerate(nums):
            diff = target-val
            if diff in d_nums:
                return [d_nums[diff], idx]
            d_nums[val] = idx
