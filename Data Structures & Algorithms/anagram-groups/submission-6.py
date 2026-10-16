class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        _sorted = []
        _map = {}
        
        for i, current in enumerate(strs):
            key = "".join(sorted(current))
            _map.setdefault(key, []).append(current)
        return _map
        
