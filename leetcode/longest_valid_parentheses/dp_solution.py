class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2 if i-2>=0 else 2
                else:
                    if i-1-dp[i-1]>=0 and s[i-1-dp[i-1]] == '(':
                        dp[i] = (dp[i-1]+dp[i-dp[i-1]-2]if i-dp[i-1]-2 >= 0 else dp[i-1]) + 2

                if dp[i] > max_len:
                    max_len = dp[i]


        return max_len
