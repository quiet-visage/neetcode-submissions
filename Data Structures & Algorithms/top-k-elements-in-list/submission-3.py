from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [v[0] for v in Counter(nums).most_common(k)]