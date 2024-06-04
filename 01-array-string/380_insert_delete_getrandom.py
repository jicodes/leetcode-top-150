import random


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_element] = last_element, idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Example usage:
# obj = RandomizedSet()
# print(obj.insert(1)) # True
# print(obj.remove(2)) # False
# print(obj.insert(2)) # True
# print(obj.getRandom()) # 1 or 2
# print(obj.remove(1)) # True
# print(obj.insert(2)) # False
# print(obj.getRandom()) # 2
