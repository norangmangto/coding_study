class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_needle = len(needle)

        if len_needle == 0:
            return 0

        for i in range(len(haystack)-len_needle+1):
            for j in range(len_needle):
                if needle[j] != haystack[i+j]:
                    break
            else:
                return i

        return -1
        
