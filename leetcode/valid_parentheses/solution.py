class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_parentheses = ['(', '{', '[']
        parenthese_match = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in open_parentheses:
                stack.append(c)
            else:  # close parentheses
                if not stack: return False  # hanlding the corner case like '())'
                pop = stack.pop()
                if parenthese_match[c] != pop:
                    return False

        return True if len(stack) == 0 else False  # handling the corner case like '(()'
