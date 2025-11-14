class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity
    
    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.table[index] == None:
                self.table[index] = Pair(key,value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.table[index].key == key:
                self.table[index].value = value
                return
            index += 1
            index = index % self.capacity


     

    def get(self, key: int) -> int:
        index = self.hash(key)
        
        while self.table[index] is not None:
            # skip tombstones
            if self.table[index] != "<deleted>" and self.table[index].key == key:
                return self.table[index].value
            
            index = (index + 1) % self.capacity

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = "<deleted>"   # tombstone to prevent broken probing
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
        
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newTable = []
        for i in range(self.capacity):
            newTable.append(None)

        oldTable = self.table
        self.table = newTable
        self.size = 0
        for pair in oldTable:
            if pair:
                self.insert(pair.key, pair.value)
