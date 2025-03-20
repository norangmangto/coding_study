class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right and max_len < left+right:
                max_len = left+right
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right and max_len < left+right:
                max_len = left+right
            elif right < left:
                left = right = 0

        return max_len
