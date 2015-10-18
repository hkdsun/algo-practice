class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        collection = []
        self.generate(collection, "", n, n)
        return collection

    def generate(self, collection, s, opened, closed):
        if opened <= 0 and closed <= 0:
            collection.append(s)
        else:
            if opened > 0:
                self.generate(collection, s+"(", opened-1, closed)
            if closed > opened:
                self.generate(collection, s+")", opened, closed-1)
