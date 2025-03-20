class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                pop = stack.pop()
                if stack:
                    if i-stack[-1] > max_len:
                        max_len = i-stack[-1]
                else: stack.append(i)

        return max_len
