class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # number of median > nums in A + number of median > nums in B == (A+B)/2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            i = (l+r)//2
            j = (m+n+1)//2 - i
            Aleft = float("-inf") if i - 1 < 0 else nums1[i-1]
            Aright = float("inf") if i >= m else nums1[i]
            Bleft = float("-inf") if j - 1 < 0 else nums2[j-1]
            Bright = float("inf") if j >= n else nums2[j]
            if Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
            else:
                if (m+n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return max(Aleft, Bleft)