class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        res = ''

        for i in range(n):
            # odd case: ex. 'aba'
            tmp_n, l, r = self.get_longest_palindrome_len(s, i, i)
            if tmp_n > max_len:
                max_len = tmp_n
                res = s[l:r+1]

            # even case: ex. 'abba'
            tmp_n, l, r = self.get_longest_palindrome_len(s, i, i+1)
            if tmp_n > max_len:
                max_len = tmp_n
                res = s[l:r+1]

        return res

    def get_longest_palindrome_len(self, s, l, r):
        n = len(s)

        while l>=0 and r<n and s[l] == s[r]:
            l, r = l-1, r+1

        return r-l-1, l+1, r-1  # (r-1)-(l+1)+1 = r-1-l-1+1 = r-l-1
