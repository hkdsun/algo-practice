class Solution(object):

    def expandPalindrome(self, s, c1, c2):
        while c1 >= 0 and c2 < len(s) and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return (c1+1, c2-1, c2-c1)

    def longestPalindrome(self, s):
        right = len(s)-1
        maxl = 0
        for i in range(len(s)):
            a, b, l = self.expandPalindrome(s, i, i)
            if l > maxl and a == 0:
                _, right, maxl = a, b, l
        for i in range(len(s)-1):
            a, b, l = self.expandPalindrome(s, i, i+1)
            if l > maxl and a == 0:
                _, right, maxl = a, b, l
        return right

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[1] + s
        b = self.longestPalindrome(s)
        suffix = s[b+1:]
        return suffix[::-1] + s

    def shortestPalindrome1(self, s):
        r = s[::-1]

        left = s[1:][::-1]
        middle = len(s) // 2 + 1
        while(middle >= 0):
            print middle
            print "1", r[len(s) - middle:], s[middle + 1:middle + 1 + middle]
            print "2", r[len(s) - middle:], s[middle:middle + middle]
            if(r[len(s) - middle:] == s[middle + 1:middle + 1 + middle]):
                print "done"
                left = s[middle + 1 + middle:][::-1]
                print left
                break
            if(r[len(s) - middle:] == s[middle:middle + middle]):
                print "done"
                left = s[middle + middle:][::-1]
                print left
                break
            middle -= 1

        return left + s

t = "abbacd"
Solution().shortestPalindrome1(t)
