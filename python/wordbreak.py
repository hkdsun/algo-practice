class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0 or len(wordDict) == 0:
            return False
        valid = [False] * (len(s)+1)
        valid[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if valid[j] and s[j:i] in wordDict:
                    valid[i] = True
                    break
        print valid
        return valid[-1]

    def wordBreak1(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        print dp
        return dp[-1]


s = "aaaaaaa"

d = ["aaaa", "aaa"]

print Solution().wordBreak(s, d)
