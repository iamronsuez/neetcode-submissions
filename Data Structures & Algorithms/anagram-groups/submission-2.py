class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        _sorted = []
        _map = {}
        
        for i, current in enumerate(strs):
            _map["".join(sorted(current))] = [i]
            for j in range(i + 1, len(strs)):
                if sorted(current) == sorted(strs[j]):
                    _map[sorted(current)].append(j)
        return _map
        
