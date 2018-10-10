class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = []
        self.data = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        self._update_queue(key)
        return self.data[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            self.data[key] = value
            self._update_queue(key)
        else:
            if self._is_full():
                poped_key = self.queue.pop(0)
                del self.data[poped_key]
            self.queue.append(key)
            self.data[key] = value

    def _update_queue(self, key):
        self.queue.append(self.queue.pop(self.queue.index(key)))

    def _is_full(self):
        return len(self.queue) == self.capacity




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
