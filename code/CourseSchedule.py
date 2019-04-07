class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dict = {}
        for course, prerequisite in prerequisites:
            dict[prerequisite] = course

        invisited =  set(range(numCourses))
        visited =set()

        while invisited:
            node = invisited.pop()
            if self.has_cycle(node, visited, invisited):
                return False
        return True


    def has_cycle(self, node, visited, invisited):
        if node in visited:
            return True
        
        for val in dict[node]:
            if val in visited:
                invisited.remove(val)
            if self.has_cycle(val, visited, invisited):
                return True

        visited.remove(node)
        return False
