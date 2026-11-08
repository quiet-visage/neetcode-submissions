from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for sz in strs:
            cache[''.join(sorted(sz))].append(sz)
            
        return list(cache.values())
