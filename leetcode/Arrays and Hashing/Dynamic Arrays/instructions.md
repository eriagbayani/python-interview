# Design Dynamic Array (Resizable Array)

## Overview

The `DynamicArray` class implements a resizable array, similar to Java's ArrayList or C++ vector. It supports automatic resizing when capacity is reached and provides common array operations.

---

## Operations

1. **Initialization**

   ```python
   DynamicArray(capacity: int)
   ```

   * Initializes an empty array with the given `capacity > 0`.
   * Internal array: `[None] * capacity`.
   * Tracks current `size` (number of elements).

---

2. **Get**

   ```python
   get(i: int) -> int
   ```

   * Returns the element at index `i`.
   * Assumes index `i` is valid.

---

3. **Set**

   ```python
   set(i: int, n: int) -> None
   ```

   * Sets the element at index `i` to `n`.
   * Assumes index `i` is valid.

---

4. **Pushback**

   ```python
   pushback(n: int) -> None
   ```

   * Adds element `n` at the end of the array.
   * If array is full (`size == capacity`), calls `resize()` before adding.

---

5. **Popback**

   ```python
   popback() -> int
   ```

   * Removes and returns the last element.
   * Assumes the array is not empty.

---

6. **Resize**

   ```python
   resize() -> None
   ```

   * Doubles the capacity of the array.
   * Creates a new internal array and copies existing elements.

---

7. **GetSize**

   ```python
   getSize() -> int
   ```

   * Returns the number of elements currently stored.

---

8. **GetCapacity**

   ```python
   getCapacity() -> int
   ```

   * Returns the current capacity of the array.

---

## Examples

### Example 1

**Input**:

```text
["Array", 1, "getSize", "getCapacity"]
```

**Output**:

```text
[null, 0, 1]
```

### Example 2

**Input**:

```text
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
```

**Output**:

```text
[null, null, 1, null, 2]
```

### Example 3

**Input**:

```text
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
```

**Output**:

```text
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
```

---

## Notes / Tips

* `pushback` triggers `resize` when array is full.
* `resize` doubles capacity and copies elements to new array.
* `get` and `set` assume valid indices (0 ≤ i < size).
* `popback` reduces `size` by 1 but does not shrink capacity.
* Internally, the array stores elements in contiguous memory and resizes dynamically as needed.
