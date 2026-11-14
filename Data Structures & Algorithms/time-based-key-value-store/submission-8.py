class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {"mood": [], "ts": []}
        self.store[key]['mood'].append(value)
        self.store[key]['ts'].append(timestamp)
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        person = self.store[key]
        ts = person['ts']
        mood = person['mood']
        left, right = 0, len(ts) - 1
        res = ""

        while (left <= right):
            mid = left + (right - left) // 2
            if ts[mid] == timestamp:
                return mood[mid]           
            if ts[mid] <= timestamp:
                left = mid + 1
                res = mood[mid]
            else:
                right = mid - 1
        return res

       