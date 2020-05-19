# -*- coding: utf-8 -*-
# @Time : 2020/5/14 7:27
# @Author : edgar
# @FileName: 127-wordlabel.py
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 2020-03-02，一刷
        # 丝毫没有思路，经典双端BFS搜索！！
        # 两端BFS搜索：一头从beginWord转换为endWord，另外一头从endWord转换为beginWord
        # 每次从中间结果少的一端出发，剪枝不必要搜索过程
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        if beginWord in wordList:
            wordList.remove(beginWord)

        res, forward, backward = 2, {beginWord}, {endWord}  # 集合的数据结构
        letters, length = set('qwertyuioplkjhgfdsazxcvbnm'), len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward  # 交换后每次都从小集合中遍历
            cur = set()  # 相当于层次序遍历中的新一层
            # 遍历每个单词，尝试替换一个字母
            for word in forward:
                for idx in range(length):
                    x, y = word[:idx], word[idx+1:]
                    # 对每个单词idx处字母尝试替换26个字符
                    for letter in letters:
                        temp = x + letter + y  # 替换掉idx处的字母
                        if temp in backward:   # 交叉重叠如dot："hit" -> "hot" -> "dot" -> "dog" -> "cog"
                            return res
                        if temp in wordList:
                            # 这里将与forward中单词只差一个字母的有效单词加入
                            # 因为该题只要求最短距离，所以已达到的都删除，避免重复访问。连visited数组都省下了
                            cur.add(temp)
                            wordList.remove(temp)
            res += 1
            forward = cur
        return 0