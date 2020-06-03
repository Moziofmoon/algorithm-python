# -*- coding: utf-8 -*-
# @Time : 2020/6/1 9:54
# @Author : edgar
# @FileName: 208-tire-tree.py

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        a = self.dic
        for i in word:
            if not i in a:
                a[i] = {}
            a = a[i]
        a["end"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        a = self.dic
        for i in word:
            if not i in a:
                return False
            a = a[i]
        if "end" in a:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        a = self.dic
        for i in prefix:
            if not i in a:
                return False
            a = a[i]
        return True


if __name__ == '__main__':
    if 15 not in range(0,10):
        print(15)
    else:
        print(5)