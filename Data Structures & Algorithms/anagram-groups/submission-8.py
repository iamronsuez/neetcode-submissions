class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = {}       
        for current in strs:
            key = "".join(sorted(current))
            _map.setdefault(key, []).append(current)
        return list(_map.values())
        
