class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        _sorted = []
        _map = {}
        
        for i, current in enumare(strs):
            _map[sorted(current)] = [i]
            for j in range(i + 1, strs):
                if sorted(current) == sorted(strs[j]):
                    _map[sorted(current)].push(j)
        return _map
        
