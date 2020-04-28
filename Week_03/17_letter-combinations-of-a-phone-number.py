# -*- coding: utf-8 -*-
# @Time : 2020/4/28 20:25
# @Author : edgar
# @FileName: 17_letter-combinations-of-a-phone-number.py

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        self.output = []
        if digits:
            self.backtrack("", digits)
        return self.output

    def backtrack(self, combination, next_digits):
        if not len(next_digits):
            self.output.append(combination)
        else:
            for letter in self.phone[next_digits[0]]:
                self.backtrack(combination + letter, next_digits[1:0])
