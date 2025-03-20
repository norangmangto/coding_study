class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        min_len = len(strs[0])
        prefix = ""

        for s in strs[1:]:
            if min_len > len(s): min_len = len(s)

        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c: return strs[0][0:i]
        else:
            return strs[0][0:min_len]
