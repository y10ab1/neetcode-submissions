class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # make sure which side is sorted/rotated
        # if nums[l] < nums[mid] --> left: sorted/ right: rotated
            # if nums[l] <= target < nums[mid] --> target in sorted part
            # else --> target in rotated part
        # else --> left: ratated/ right: sorted
            # if nums[mid] < target < nums[r] --> target in sorted part
            # else --> target in rotated part

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # left sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        #            t
        # # [3 4 5 6 1 2]
        #    l   m     r 
        #          l m r
        #          l r
        #         lm r

