class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        _sorted = []
        _map = {}
        
        for i, current in enumerate(strs):
            _map["".join(sorted(current))].setdefault(i, [])
            if sorted(current) == sorted(strs[i]):
                    _map["".join(sorted(current))].append(i)
        return []
        
