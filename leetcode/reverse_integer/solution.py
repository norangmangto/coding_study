class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647;
        INT_MIN = 2147483648;  # actually it is -2147483648
                               # but change it because in python,
                               # modulo works differently with c's modulo

        m, LIMIT = (x, INT_MAX) if x > 0 else (-1*x, INT_MIN)
        rev = 0

        while m!=0:
            if rev > LIMIT//10 or (rev == LIMIT//10 and m%10 > LIMIT%10): return 0
            rev = rev*10 + m%10
            m = m // 10

        return rev if x > 0 else -1*rev
