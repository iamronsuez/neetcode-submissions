from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        i = bisect_right(pairs, timestamp, key=lambda p:p[1])   # cuántos timestamps son <= timestamp
        return pairs[i - 1][0] if i else ""

       