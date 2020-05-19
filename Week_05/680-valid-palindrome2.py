# -*- coding: utf-8 -*-
# @Time : 2020/5/19 8:58
# @Author : edgar
# @FileName: 680-valid-palindrome2.py


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                s1 = s[:left] +s[left + 1:]
                s2 = s[:right] +s[right + 1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            left += 1
            right -= 1

    if __name__ == '__main__':
        s = "abcd"
        print(s[::-1])
