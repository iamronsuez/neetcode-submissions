class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
            
    def get(self, key: str, timestamp: int) -> str:
        res, person = "", self.store.get(key, [])
        left, right = 0, len(person) - 1
        res = ""
        while (left <= right):
            mid = left + (right - left) // 2
            if person[mid][1] == timestamp:
                return person[mid][0]          
            if person[mid][1] <= timestamp:
                left = mid + 1
                res = person[mid][0]
            else:
                right = mid - 1
        return res

       