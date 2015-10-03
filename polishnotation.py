class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        while tokens:
            t = tokens.pop(0)
            if t in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                res = 0
                if t == "+":
                    res = op1 + op2
                elif t == "*":
                    res = op1 * op2
                elif t == "/":
                    res = op2 / op1
                else:
                    res = op2 - op1
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]

s = ["2", "1", "+", "3", "*"]
s1 = ["4", "13", "5", "/", "+"]
s2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print Solution().evalRPN(s)
print Solution().evalRPN(s1)
print Solution().evalRPN(s2)
