#!/usr/bin/python3
# https://leetcode.com/problems/lru-cache/
from typing import List
from collections import OrderedDict


class LRUCacheWithQueue:
    def __init__(self, capacity: int):
        self.size: int = capacity
        self.queue: List[int] = []  # store key to maintain order
        self.store = {}

    def get(self, key: int) -> int:
        value = self.store.get(key, -1)
        if value != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.queue) == self.size and key not in self.store:  # evict the least recently used key
            evicted_key = self.queue.pop(0)
            del self.store[evicted_key]

        if key in self.store:
            self.queue.remove(key)

        self.store[key] = value
        self.queue.append(key)


class LRUCacheWithOrderedDict:
    def __init__(self, capacity: int):
        self.size: int = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


if __name__ == '__main__':
    pass
