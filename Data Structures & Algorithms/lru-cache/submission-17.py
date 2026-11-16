class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}     # llave → valor
        self.usage = {}       # llaves: [menos reciente, ..., más reciente]
        self.tick = 0

    def get(self, key):
        if key not in self.storage:
            return -1
        # en get y en put
        self.tick += 1
        self.usage[key] = self.tick     # "esta llave se usó a esta hora"
        return self.storage[key]

    def put(self, key, value):
        self.storage[key] = value
        # en get y en put
        self.tick += 1
        self.usage[key] = self.tick     # "esta llave se usó a esta hora"
        if len(self.storage) > self.capacity:
            old = min(self.usage, key = self.usage.get)     # la menos reciente: ¿en qué extremo de order está?
            del self.storage[old]
            del self.usage[old]

