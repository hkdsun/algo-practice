# Definition for a binary tree node.
# class TreeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        right = True
        res = []
        while queue:
            node = queue.pop(0)
            if len(queue) == 0:
                right = not right
            if right:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += [node.val]
        return res

root = TreeNode(3)
r20 = TreeNode(20)
r9 = TreeNode(9)
r8 = TreeNode(8)
r15 = TreeNode(15)
r7 = TreeNode(7)
r4 = TreeNode(
r3 = TreeNode(
r2 = TreeNode(
r19 = TreeNode(
r25 = TreeNode(
