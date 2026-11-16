class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}     # llave → valor
        self.order = []       # llaves: [menos reciente, ..., más reciente]

    def get(self, key):
        if key not in self.storage:
            return -1
        self.order.remove(key)
        self.order.append(key)                # marcar key como la más reciente en order
        return self.storage[key]

    def put(self, key, value):
        if key in self.storage:
            self.order.remove(key)            # ya existía: sacarla de su lugar en order
        self.storage[key] = value
        self.order.append(key)                # ponerla al final de order: la más reciente
        if len(self.storage) > self.capacity:
            old = self.order.pop(0)     # la menos reciente: ¿en qué extremo de order está?
            del self.storage[old]

