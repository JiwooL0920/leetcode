class MyHashSet:

    def __init__(self):
        # Space: O(N)
        self.mapp = {}

    def add(self, key: int) -> None:
        # Time: O(1)
        self.mapp[key] = 0

    def remove(self, key: int) -> None:
        # Time: O(1)
        if key in self.mapp:
            del self.mapp[key]

    def contains(self, key: int) -> bool:
        # Time: O(1)
        return key in self.mapp


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
