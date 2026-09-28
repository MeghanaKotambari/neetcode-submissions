from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        # Add to the end = most recently used
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_lru(self):
        if self.head.next == self.tail:
            return None

        node = self.head.next
        self.remove(node)
        return node

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        # key -> Node
        self.cache = {}

        # frequency -> DLL
        self.freq = defaultdict(DLL)

    def update(self, node):
        old_freq = node.freq

        # Remove from old frequency list
        self.freq[old_freq].remove(node)

        # If it was the minimum frequency and became empty
        if old_freq == self.min_freq and self.freq[old_freq].is_empty():
            self.min_freq += 1

        # Increase frequency
        node.freq += 1

        # Add to new frequency list
        self.freq[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.update(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Existing key
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.update(node)
            return

        # Cache is full
        if self.size == self.capacity:
            lfu_list = self.freq[self.min_freq]

            # Remove LRU node from minimum-frequency list
            node = lfu_list.remove_lru()

            del self.cache[node.key]
            self.size -= 1

        # Insert new node
        node = Node(key, value)

        self.cache[key] = node
        self.freq[1].add(node)

        self.min_freq = 1
        self.size += 1