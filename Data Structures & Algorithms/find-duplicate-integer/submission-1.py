class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        start = 0
        while True:
            slow = nums[slow]
            start = nums[start]
            if start == slow:
                return start
