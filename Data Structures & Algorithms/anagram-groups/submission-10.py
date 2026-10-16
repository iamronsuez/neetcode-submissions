class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for current in strs:
            count = [0] * 26
            for c in current:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(current)
        return list(groups.values())

