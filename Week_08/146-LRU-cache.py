# -*- coding: utf-8 -*-
# @Time : 2020/6/13 21:05
# @Author : edgar
# @FileName: 146-LRU-cache.py
import collections


class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)

    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)

    cache.get(4)
