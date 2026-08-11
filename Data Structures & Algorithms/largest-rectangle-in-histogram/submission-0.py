class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                sheight, sindex = stack.pop()
                maxarea = max(maxarea, (i-sindex) * sheight)
                start = sindex
            stack.append((h,start))
        
        while stack:
            height, start = stack.pop()
            maxarea = max(maxarea, height * (len(heights)-start))
        return maxarea