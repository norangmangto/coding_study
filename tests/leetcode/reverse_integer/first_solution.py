class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        max = pow(2, 31)-1
        min = -pow(2, 31)
        sign = ''
        strX = str(x)
        if strX[0] == '-':
            sign = '-'
            strX = strX[1:]
        newX = int(sign + strX[::-1])
        if newX < min:
            newX = 0
        if newX > max:
            newX = 0

        return newX
