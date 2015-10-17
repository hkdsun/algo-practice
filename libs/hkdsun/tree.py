# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def tree(nodes):
        if isinstance(nodes[0], int):
            nodes = map(lambda x: TreeNode(x) if x is not None else None, nodes)
        m = len(nodes)/2
        for i in range(m):
            if nodes[i] is not None:
                if (i*2)+1 < len(nodes) and nodes[(i*2)+1]:
                    nodes[i].left = nodes[(i*2)+1]
                if (i*2)+2 < len(nodes) and nodes[(i*2)+2]:
                    nodes[i].right = nodes[(i*2)+2]
        return nodes[0]

    @staticmethod
    def pre_order(root):
        if root:
            print root.val
            TreeNode.pre_order(root.left)
            TreeNode.pre_order(root.right)
