# Implement a set data structure with the following methods:

# CustomSet() constructs a new instance of a set
# add(int val) adds val to the set
# exists(int val) returns whether val exists in the set
# remove(int val) removes the val in the set
# This should be implemented without using built-in set.

# Lookup T: O(1) --> dictionary
class CustomSet:
    def __init__(self):
        self.items = {}

    def add(self, val):
        if not self.exists(val):
            self.items[val] = 1

    def exists(self, val):
        try:
            key = self.items[val]
            return True
        except:
            return False

    def remove(self, val):
        if self.exists(val):
            del self.items[val]
        