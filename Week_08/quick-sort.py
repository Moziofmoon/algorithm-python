# -*- coding: utf-8 -*-
# @Time : 2020/6/19 7:44
# @Author : edgar
# @FileName: quick-sort.py

class Solution:
    def quickSort(self, array, begin, end):
        if end <= begin:
            return
        pivot = self.partiton(array, begin, end)
        self.quickSort(array, begin, pivot - 1)
        self.quickSort(array, pivot + 1, end)

    def partiton(self, array, begin, end):
        pivot = end
        counter = begin
        for i in range(begin, end):
            if(array[i] < array[pivot]):
                array[counter], array[i] = array[i], array[counter]
                counter += 1

        array[pivot], array[counter] = array[counter], array[pivot]
        return counter

if __name__ == '__main__':
    solution = Solution()
    arr = [3, 1, 4, 7, 2]
    solution.quickSort(arr, 0, len(arr) - 1)
    print(arr)

