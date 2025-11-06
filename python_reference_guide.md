# Python Learning Reference Guide

## Variables - Dynamically Typed

Python is a dynamically typed language, so you don't have to declare variable types.

```python
n = 0
print('n =', n)  # n = 0

# Types are determined at run time
n = "abc"
print('n =', n)  # n = abc
```

### Multiple Assignments

You can assign multiple variables in a single line, with different types.

```python
n, m = 0, 'abc'
```

### Incrementing

```python
n = n + 1  # good
n += 1     # also good
# n++      # This will NOT work in Python
```

### None - The Absence of Value

Python's version of null is called `None`.

```python
n = 4
n = None
print('n =', n)  # n = None
```

## If Statements

No parentheses or curly braces needed - Python uses indentation.

```python
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
print('n =', n)  # n = 3
```

### Multi-line Conditions

Parentheses are needed for multi-line conditions. Note: `and` = `&&`, `or` = `||`

```python
n, m = 1, 2
if ((n > 2 and 
    n != m) or n == m):
    n += 1
```

## While Loops

```python
n = 0
while n < 5:
    print(n)  # 0 1 2 3 4
    n += 1
```

## For Loops

```python
# Looping from i = 0 to i = 4
for i in range(5):
    print(i)  # i is incremented implicitly

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Going in reverse, i = 5 to i = 2
for i in range(5, 1, -1):  # Third argument is decrement
    print(i)
```

## Math Operations

### Division

Division is decimal by default.

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2 (rounds down)

# CAREFUL: Most languages round towards 0, but Python rounds down
print(-3 // 2)  # -2

# WORKAROUND: Use decimal division and convert to int
print(int(-3 / 2))  # -1
```

### Modulo

```python
print(10 % 3)   # 1
print(-10 % 3)  # 2 (different from most languages!)

# To be consistent with other languages:
import math
print(math.fmod(-10, 3))  # -1.0
```

### Math Helpers

```python
import math

print(math.floor(3 / 2))  # 1 (explicitly round down)
print(math.ceil(3 / 2))   # 2 (explicitly round up)
print(math.sqrt(2))       # 1.414...
print(math.pow(2, 3))     # 8.0 (2^3)
```

### Max / Min Int

```python
float("inf")   # Maximum integer
float("-inf")  # Minimum integer

# Python numbers are infinite - they never overflow
print(math.pow(2, 200))  # Very large number
print(math.pow(2, 200) < float("inf"))  # True
```

## Arrays (Lists in Python)

Arrays in Python are dynamic by default and can be used as stacks.

```python
arr = [1, 2, 3]

# Push to array (append)
arr.append(4)  # [1, 2, 3, 4]
arr.append(5)  # [1, 2, 3, 4, 5]

# Pop (at the end)
arr.pop()  # [1, 2, 3, 4]

# Insert at the middle (O(n) operation)
arr.insert(1, 7)  # [1, 7, 2, 3, 4]

# Indexing (constant time operation)
arr[0] = 0
arr[3] = 0  # [0, 7, 2, 0, 4]

# Initialize array of size n with default value
n = 5
arr = [1] * n
print(arr)      # [1, 1, 1, 1, 1]
print(len(arr)) # 5

# Negative indexing
arr = [1, 2, 3]
print(arr[-1])  # 3 (last value)
print(arr[-2])  # 2 (second to last)
```

### Slicing

```python
arr = [1, 2, 3, 4]
print(arr[1:3])  # [2, 3] (start at index 1, stop before index 3)
print(arr[0:4])  # [1, 2, 3, 4]
```

### Unpacking

```python
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3
# Be careful: number of variables must match array length
```

### Looping Through Arrays

```python
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With both index and value
for i, n in enumerate(nums):
    print(i, n)  # 0 1, 1 2, 2 3
```

### Loop Through Multiple Arrays

```python
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)  # 1 2, 3 4, 5 6
```

### Sorting and Reversing

```python
# Reverse
nums = [1, 2, 3]
nums.reverse()  # [3, 2, 1]

# Sort ascending
arr = [5, 4, 7, 3, 8]
arr.sort()  # [3, 4, 5, 7, 8]

# Sort descending
arr.sort(reverse=True)  # [8, 7, 5, 4, 3]

# Sort strings (alphabetical by default)
arr = ['bob', 'alice', 'jane', 'doe']
arr.sort()  # ['alice', 'bob', 'doe', 'jane']

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))  # ['bob', 'doe', 'jane', 'alice']
```

### List Comprehension

```python
arr = [i for i in range(5)]  # [0, 1, 2, 3, 4]
```

### 2D Lists

```python
arr = [[0] * 4 for i in range(4)]
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

## Strings

Strings are similar to arrays but immutable.

```python
s = 'abc'
print(s[0:2])  # ab

# IMMUTABLE - cannot modify
# s[0] = "A"  # This will error!

# You can create a new string
s += 'def'
print(s)  # abcdef
# Note: Any modification creates a new string (O(n) time)
```

### String Conversions

```python
# String to int
print(int("123") + int("123"))  # 246

# Int to string
print(str(123) + str(123))  # 123123
```

### ASCII Values

```python
print(ord("a"))  # 97
print(ord("b"))  # 98
```

### Joining Strings

```python
strings = ["ab", "cd", "ef"]
print("".join(strings))  # abcdef
```

## Queues (Double-Ended)

Python queues are double-ended by default.

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)  # deque([1, 2])

# Pop from left (constant time)
queue.popleft()
print(queue)  # deque([2])

# Add to left
queue.appendleft(1)
print(queue)  # deque([1, 2])

# Pop from right
queue.pop()
print(queue)  # deque([1])
```

## HashSet

Search and insert in constant time, no duplicates allowed.

```python
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)     # {1, 2}
print(len(mySet)) # 2

# Search using 'in' operator
print(1 in mySet)  # True
print(2 in mySet)  # True
print(3 in mySet)  # False

# Remove
mySet.remove(2)
print(2 in mySet)  # False

# List to set
print(set([1, 2, 3]))  # {1, 2, 3}

# Set comprehension
mySet = {i for i in range(5)}  # {0, 1, 2, 3, 4}
```

## HashMap (Dictionary)

```python
myMap = {}

# Insert
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)      # {'alice': 88, 'bob': 77}
print(len(myMap)) # 2

# Modify
myMap['alice'] = 80
print(myMap['alice'])  # 80

# Search
print("alice" in myMap)  # True

# Remove
myMap.pop("alice")
print("alice" in myMap)  # False

# Initialize with values
myMap = {'alice': 90, 'bob': 100}

# Dict comprehension
myMap = {i: 2*i for i in range(3)}  # {0: 0, 1: 2, 2: 4}
```

### Looping Through Maps

```python
myMap = {'alice': 90, 'bob': 70}

# Keys and values
for key in myMap:
    print(key, myMap[key])

# Values only
for val in myMap.values():
    print(val)

# Items (key-value pairs)
for key, value in myMap.items():
    print(key, value)
```

## Tuples

Like arrays but immutable - cannot be changed after creation.

```python
tup = (1, 2, 3)
print(tup)     # (1, 2, 3)
print(tup[0])  # 1
print(tup[-1]) # 3

# Cannot modify
# tup[0] = 0  # Won't work, immutable

# Can be used as keys in hash map/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])  # 3

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)  # True

# Lists CANNOT be keys
# myMap[[3, 4]] = 5  # This will error!
```

## Heaps

Find min/max of values frequently. Implemented with arrays under the hood.

```python
import heapq

# Min Heap (default in Python)
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Minimum is always at index 0
print(minHeap[0])  # 2

# Pop values (smallest to largest)
while len(minHeap):
    print(heapq.heappop(minHeap))  # 2, 3, 4
```

### Max Heap Workaround

Python doesn't have max heaps by default. Multiply by -1 when pushing and popping.

```python
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is at index 0
print(-1 * maxHeap[0])  # 4

# Pop values (largest to smallest)
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))  # 4, 3, 2
```

### Build Heap from Array

You can heapify in linear time.

```python
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))  # 1, 2, 4, 5, 8
```

## Functions

```python
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))  # 12
```

### Nested Functions

Nested functions have access to outer variables.

```python
def outer(a, b):
    c = 'c'
    
    def inner():
        return a + b + c
    
    return inner()

print(outer("a", "b"))  # abc
```

### Modifying Variables in Nested Functions

```python
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # To modify value outside helper scope, use nonlocal
        nonlocal val
        val *= 2
    
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)  # [2, 4] 6
```

## Classes

```python
class MyClass:
    # Constructor
    def __init__(self, nums):  # self is passed in every method
        self.nums = nums
        self.size = len(nums)
    
    # Methods require self as parameter
    def getLength(self):
        return self.size
    
    # Calling another member function
    def getDoubleLength(self):
        return 2 * self.getLength()

# Usage
obj = MyClass([1, 2, 3])
print(obj.getLength())       # 3
print(obj.getDoubleLength()) # 6
```