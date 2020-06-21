# -*- coding: utf-8 -*-
# @Time : 2020/6/20 7:57
# @Author : edgar
# @FileName: merge-sort.py

class Solution:
    def mergeSort(self, array, left, right):
        if right <= left:
            return
        mid = (left + right) >> 1

        self.mergeSort(array, left, mid)
        self.mergeSort(array, mid + 1, right)
        self.merge(array, left, mid, right)

    def merge(self, array, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        k = 0
        while i <= mid and j <= right:
            if array[i] <= array[j]:
                temp.append(array[i])
                i += 1
            else:
                temp.append(array[j])
                j += 1

        while i <= mid:
            temp.append(array[i])
            i += 1
        while j <= right:
            temp.append(array[j])
            j += 1

        array[left:right+1] = temp


if __name__ == '__main__':
    solution = Solution()
    arr = [3, 1, 4, 7, 2]
    solution.mergeSort(arr, 0, len(arr) - 1)
    print(arr)

