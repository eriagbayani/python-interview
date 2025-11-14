class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity     # maximum number of elements without resizing
        self.length = 0              # current number of elements
        self.array = [0] * capacity  # internal storage

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.array[self.length] = n
        self.length += 1
        

    def popback(self) -> int:
       last_elem = self.array[self.length - 1]
       self.length -= 1
       return last_elem

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 

        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.array[i]
        self.array = newArr


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
