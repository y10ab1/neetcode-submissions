class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = defaultdict(list)
        for n,v in count.items():
            freq[v].append(n)

        res = []
        for f in sorted(freq.keys())[::-1]:
            res += freq[f]
            if len(res) == k:
                return res