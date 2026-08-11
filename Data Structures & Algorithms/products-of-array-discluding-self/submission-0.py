class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_rl, prod_lr = [1] * len(nums), [1] * len(nums)
        for i, n in enumerate(nums):
            prod_lr[i] *= prod_lr[i-1] * n
            prod_rl[len(nums)-1-i] *= prod_rl[(len(nums)-i)%len(nums)] * nums[len(nums)-1-i]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(prod_rl[i+1])
            elif i == len(nums) - 1:
                res.append(prod_lr[i-1])
            else:
                res.append(prod_lr[i-1]*prod_rl[i+1])
        return res