class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for idx in range(len(freq)-1,0,-1):
            res += freq[idx]
            if len(res) == k:
                return res