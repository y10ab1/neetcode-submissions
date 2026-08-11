class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, val):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = val

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)