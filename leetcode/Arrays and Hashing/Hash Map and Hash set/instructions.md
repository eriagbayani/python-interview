# Design Hash Table

## Overview

The `HashTable` class implements a hash table (open addressing with linear probing) that supports the following operations:

1. **Initialization**

   ```python
   HashTable(capacity: int)
   ```

   * Creates an empty hash table with a given `capacity > 1`.
   * Internal array: `[None] * capacity`.
   * Tracks current `size` (number of keys stored).

---

2. **Insert / Update**

   ```python
   insert(key: int, value: int) -> None
   ```

   * Inserts a key-value pair.
   * If the key already exists, updates its value.
   * **Collision handling**: Linear probing.
   * Automatically calls `resize()` if load factor ≥ 0.5:

     ```python
     load_factor = size / capacity
     if load_factor >= 0.5: resize()
     ```
   * Tombstones (`"<deleted>"`) are reused for new inserts.

---

3. **Get**

   ```python
   get(key: int) -> int
   ```

   * Returns the value associated with `key`.
   * Returns `-1` if the key is not present.
   * Skips deleted slots while probing.

---

4. **Remove**

   ```python
   remove(key: int) -> bool
   ```

   * Removes the key-value pair with the given key.
   * Returns `True` if removed, `False` if key not present.
   * Uses tombstone marker `"<deleted>"` to maintain probe chain.

---

5. **GetSize**

   ```python
   getSize() -> int
   ```

   * Returns the number of keys currently stored.

---

6. **GetCapacity**

   ```python
   getCapacity() -> int
   ```

   * Returns the current capacity of the hash table.
   * Capacity doubles automatically after `resize()`.

---

7. **Resize**

   ```python
   resize() -> None
   ```

   * Doubles the table capacity.
   * Re-inserts all valid elements into the new table.
   * Automatically called by `insert()` when load factor ≥ 0.5.

---

## Collision Handling

* Open addressing with **linear probing**.
* Tombstones (`"<deleted>"`) allow probing to continue correctly after removal.

---

## Example 1

**Input**:

```text
["HashTable", 4, "insert", 1, 2, "get", 1, "insert", 1, 3, "get", 1, "remove", 1, "get", 1]
```

**Output**:

```text
[null, null, 2, 3, true, -1]
```

**Explanation**:

* Insert (1,2) → store key 1.
* Get 1 → returns 2.
* Insert (1,3) → updates value.
* Get 1 → returns 3.
* Remove 1 → returns true.
* Get 1 → returns -1 (not found).

---

## Example 2

**Input**:

```text
["HashTable", 2, "getCapacity", "insert", 6, 7, "getCapacity", "insert", 1, 2, "getCapacity", "insert", 3, 4, "getCapacity", "getSize"]
```

**Output**:

```text
[null, 2, null, 4, null, 8, null, 8, 3]
```

**Explanation**:

* Start capacity = 2.
* Insert 6,7 → size=1, load factor=0.5 → triggers resize → capacity=4.
* Insert 1,2 → size=2 → load factor=0.5 → triggers resize → capacity=8.
* Insert 3,4 → size=3 → load factor < 0.5 → no resize.
* GetSize → returns 3.

---

## Notes / Tips

* **Linear probing** requires handling tombstones during insert/get/remove.
* **Load factor** triggers `resize()` correctly at 0.5.
* After `resize()`, all old keys must be re-inserted to maintain correct hashing.
* Always check for tombstones in `get()` and `insert()` to avoid attribute errors.
* The internal `Pair` class stores key-value pairs for table entries.
