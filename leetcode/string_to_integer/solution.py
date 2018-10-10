class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        # find non-space character. (we can use s.strip() also)
        for i, c in enumerate(s):
            if c != ' ':
                s = s[i:]
                break
        else:
            return 0
        # alternative codes of below are followings
        # s = s.strip()
        # if len(s) == 0: return 0

        INT_MAX = 2147483647;
        INT_MIN = 2147483648;
        if s[0] != '-':
            if s[0] == '+': s = s[1:]  # Unexpected case: starting with '+'
            is_positive = True
            LIMIT = INT_MAX
        else:
            s = s[1:]
            is_positive = False
            LIMIT = INT_MIN

        rev = 0
        for c in s:
            if not c.isdigit():
                break

            if rev > LIMIT//10 or (rev == LIMIT//10 and int(c) > LIMIT%10):
                return INT_MAX if is_positive else -1*INT_MIN

            rev = 10*rev + int(c)

        return rev if is_positive else -1*rev
