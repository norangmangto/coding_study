class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647;
        INT_MIN = -2147483648;

        if x>INT_MAX or x<INT_MIN: return 0

        m = x if x>0 else -1*x
        rev = 0

        while m>0:
            rev = rev*10 + m%10
            m = m // 10

        if x<0: rev = -1*rev

        return 0 if rev>INT_MAX or rev<INT_MIN else rev
        
