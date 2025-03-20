class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        basic_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        need_to_check = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        res = 0
        prev = None
        for c in s:
            res += basic_map[c]
            if prev in need_to_check and c in need_to_check[prev]:
                res -= basic_map[prev] * 2
            prev = c

        return res
