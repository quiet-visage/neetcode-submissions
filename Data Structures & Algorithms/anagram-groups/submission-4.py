class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        if len(strs) < 2:
            return [strs]

        cache = {}

        for sz in strs:
            sz_srtd = ''.join(sorted(sz))
            if sz_srtd in cache:
                cache[sz_srtd].append(sz)
            else:
                cache[sz_srtd] = [sz]
            
        return list(cache.values())
