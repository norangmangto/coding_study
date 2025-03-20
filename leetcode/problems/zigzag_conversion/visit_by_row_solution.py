class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        r = ""
        jump_len = numRows + (numRows-2)

        for i in range(numRows):
            if i == 0:  # 0 row (first row)
                j = i
                while j < len(s):
                    r += s[j]
                    j += jump_len
            elif i != numRows-1:  # 1~numRows-2 rows
                j = i
                while j < len(s):
                    r += s[j]
                    extra = j + jump_len - (i*2)
                    if extra < len(s):
                        r += s[extra]
                    j += jump_len
            else:    # numRows- row (last row)
                j = i
                while j < len(s):
                    r += s[j]
                    j += jump_len

        return r
