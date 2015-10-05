class Solution(object):
    def findOrder(self, numCourses, prereqs):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degrees = {}
        edges = {}

        for i in range(numCourses):
            in_degrees[i] = 0

        for prereq in prereqs:
            in_degrees[prereq[0]] += 1
            if prereq[1] in edges:
                edges[prereq[1]].append(prereq[0])
            else:
                edges[prereq[1]] = [prereq[0]]

        queue = []

        for k, v in in_degrees.iteritems():
            if v == 0:
                queue.append(k)

        print queue
        head = 0
        while len(queue) != numCourses and head < len(queue):
            cur = queue[head]
            if cur in edges:
                for n in edges[cur]:
                    in_degrees[n] -= 1
                    if in_degrees[n] == 0:
                        queue.append(n)
            head += 1

        if len(queue) == numCourses:
            return queue
        else:
            return []
