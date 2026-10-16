class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        h = []
        for n in nums:
            counts[n] +=1

        for n, freq in counts.items():
            heapq.heappush(h, (freq, n)) 
            if len(h) > k:
                heapq.heappop(h)
        return [n for freq, n in h]        