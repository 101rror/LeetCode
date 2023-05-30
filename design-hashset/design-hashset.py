class MyHashSet:

    def __init__(self):
        self.map = defaultdict(int)
        
    def add(self, key: int) -> None:
        self.map[key] = True

    def remove(self, key: int) -> None:
        self.map[key] = False

    def contains(self, key: int) -> bool:
        return self.map[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)