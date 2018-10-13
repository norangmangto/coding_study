class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows == 1 or n <= numRows: return s

        n = len(s)
        direction = 1
        pool = [['' for _ in range(numRows)]]
        i = 0

        for c in s:
            if direction < 0:  # backward
                pool.append(['' for _ in range(numRows)])
            pool[-1][i] = c
            i += direction
            if i == numRows or i < 0:
                direction = -1*direction
                if direction < 0:
                    i = numRows - 2
                else:
                    i = 1

        ret_ch_list = []
        for i in range(numRows):
            for j in range(len(pool)):
                if pool[j][i] != '':
                    ret_ch_list.append(pool[j][i])

        return ''.join(ret_ch_list)
