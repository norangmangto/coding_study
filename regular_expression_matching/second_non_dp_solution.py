class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def non_dp(i, j):
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    ans = non_dp(i, j+2) or first_match and non_dp(i+1, j)
                else:
                    ans = first_match and non_dp(i+1, j+1)

            return ans

        return non_dp(0, 0)
