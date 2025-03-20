class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2: return n

        max_len = 0
        start = 0
        hash_map = {}
        for end in range(n):
            if s[end] in hash_map:
                if end-start > max_len:
                    max_len = end-start
                while s[start] != s[end]:
                    del hash_map[s[start]]
                    start += 1
                else:
                    del hash_map[s[start]]
                    start += 1

            hash_map[s[end]] = 1

        if end-start+1 > max_len:
            max_len = end+1-start

        return max_len
