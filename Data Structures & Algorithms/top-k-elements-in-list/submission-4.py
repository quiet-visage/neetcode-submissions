from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bkt = {}
        for n in nums:
            if n in bkt:
                bkt[n] += 1
            else:
                bkt[n] = 1
        
        cvrtd = list(bkt.items())
        srtd = sorted(cvrtd, key=lambda x: x[1], reverse=True)
        return [v[0] for v in srtd[:k]]
