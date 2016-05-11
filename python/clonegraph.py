# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        visited = set()
        q1, q2 = [node], [UndirectedGraphNode(node.label)]
        while q1:
            head, cur = q1.pop(0), q2.pop(0)
            if head not in visited:
                visited.add(head)
                for ne in head.neighbours:
                    c = UndirectedGraphNode(ne.label)
                    cur.neighbors.append(c)
                    q2.append(c)
                    q1.append(ne)


n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)

n0.neighbors = [n1, n2]
n1.neighbors = [n2]
n2.neighbors = [n2]
