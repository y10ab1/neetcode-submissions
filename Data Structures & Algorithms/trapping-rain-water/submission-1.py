class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        ans = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] < lmax:
                    ans += lmax - height[l]
                lmax = max(lmax, height[l])
            else:
                r -= 1
                if height[r] < rmax:
                    ans += rmax - height[r]
                rmax = max(rmax, height[r])
        return ans