class RandomizedSet:
    def __init__(self):
        self.num_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        index = self.num_to_index[val]
        last_element = self.nums[-1]
        self.nums[index] = last_element
        self.num_to_index[last_element] = index
        self.nums.pop()
        del self.num_to_index[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
