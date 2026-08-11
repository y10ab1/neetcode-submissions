class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)

            if i >= k-1:
                ans.append(nums[q[0]])
            if i - k + 1 == q[0]:
                q.popleft()
        
        return ans