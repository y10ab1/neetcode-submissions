class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(n) for checking if valid
        # O(logn) for binary search
        # Total O(nlogn)
        l, r = 1, max(piles)
        mink = r
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            if time > h:
                l = mid + 1
            else:
                mink = min(mink, mid)
                r = mid - 1
        return mink

    ############
    # Input: piles = [25,10,23,4], h = 4
    # mid: (4+25)/2 = 14
    # 2+1+2+1 = 6 > 4

    # mid: (15+25)//2 = 20
    # 2+1+2+1 = 6 > 4

    # mid: 22
    # 2 1 2 1

    # mid: 23
    # 2 1 1 1 = 5 > 4

    # mid: 24
    # 2 1 1 1 = 5 > 4

    # mid: 25
    # 1 1 1 1 = 4 = 4