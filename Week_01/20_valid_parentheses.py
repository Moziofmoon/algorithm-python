class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in dic.values():
                stack.append(char)
            if char in dic.keys() and dic[char] == stack[-1]:
                    stack.pop()

        if stack:
            return False
        else:
            return True


class Solution2:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']

        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False

        return len(stack) == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
