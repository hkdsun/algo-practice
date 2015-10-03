# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, curLevel, nextLevel, right = [], [root], [], True
        while curLevel:
            l = list(x.val for x in curLevel)
            if right:
                res.append(l)
            else:
                l.reverse()
                res.append(l)
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            curLevel, nextLevel, right = nextLevel, [], not right
        return res

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

print Solution().zigzagLevelOrder(n3)
