class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = list(s)
        while queue:
            operand_left = ""
            while len(queue) != 0 and queue[0] in " 0123456789":
                operand_left += queue.pop(0)
            if len(queue) == 0:
                return operand_left
            operand_left = int(operand_left.strip())
            operator = ""
            while queue[0] in " +-/*":
                operator += queue.pop(0)
            operator = operator.strip()
            operand_right = ""
            while len(queue) != 0 and queue[0] in " 0123456789":
                operand_right += queue.pop(0)
            operand_right = int(operand_right.strip())
            res = 0
            if operator is "*":
                res = operand_left * operand_right
            elif operator is "/":
                res = operand_left / operand_right
            queue = list(str(res)) + queue

print Solution().calculate("3*3*3/3")
