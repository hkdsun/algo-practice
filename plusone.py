class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            v = digits[i] + carry
            v, carry = (0, 1) if v == 10 else (v, 0)
            digits[i] = v
            if not carry:
                return digits
        if carry:
            return [1] + digits

print Solution().plusOne([9,9,9])
