class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mi = []
        self.le = 0
        self.mile = 0


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)
        if self.mile == 0:
            self.mi += [x]
            self.mile += 1
        elif x < self.mi[self.mile-1]:
            self.mi += [x]
            self.mile += 1
        self.le += 1



    def pop(self):
        """
        :rtype: nothing
        """
        self.data.pop()
        if x == self.mi[len(mi)-1]:
            self.mi.pop()
            self.mile -= 1
        self.le -= 1


    def top(self):
        """
        :rtype: int
        """
        return self.data[self.le-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.mi[self.mile-1]

s = MinStack()
s.top is None
s.push(3)
s.push(1)
s.push(2)
print s.top() == 3
print s.getMin()
print s.data
print s.mi
