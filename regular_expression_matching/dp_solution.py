import unittest

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]
            
        return dp(0, 0)

class TestSolution(unittest.TestCase):
    def test_all_none(self):
        s = ""
        p = ""
        self.assertTrue(Solution().isMatch(s, p))

    def test_none_string(self):
        s = ""
        p = "a"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_with_equal_length(self):
        s = "abcd"
        p = "defg"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_symbol_not_equal_with_not_equal_length(self):
        s = "abcd"
        p = "abcde"
        self.assertFalse(Solution().isMatch(s, p))

    def test_no_test_symbol_pattern(self):
        s = ""
        p = "ab*"
        self.assertFalse(Solution().isMatch(s, p))

    def test_matched_symbol_pattern_1(self):
        s = "ab"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_matched_symbol_pattern_2(self):
        s = "a"
        p = "ab*"
        self.assertTrue(Solution().isMatch(s, p))

    def test_not_matched_duplicated_pattern(self):
        s = "aaaaaaaaab"
        p = "a*a*a*a*a*a*a*a*a*a*c"
        self.assertFalse(Solution().isMatch(s, p))

if __name__ == "__main__":
    unittest.main()
