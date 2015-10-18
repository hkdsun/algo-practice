class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if d[c] != stack.pop():
                    return False
        return len(stack) == 0

l = "(])"
print Solution().isValid(l)
