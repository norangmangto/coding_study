class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        if n == 0: return ""
        elif n == 1: return s[0]

        dp = [[False for x in range(n)] for x in range(n)]

        max_len = 0
        start = 0

        for cl in range(1, n+1):
            for i in range(n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and (cl < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if cl > max_len:
                        max_len = cl
                        start = i

        return s[start:start+max_len]
