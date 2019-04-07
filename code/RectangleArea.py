import math
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = self.area(A, B, C, D) + self.area(E, F, G, H)

        if self.is_overlap(A, B, C, D, E, F, G, H):
            overlap = min((C-E),(G-A),(C-A),(G-E))*min((D-B),(H-F),(H-B),(D-F))
            return total - overlap
        else:
            return total

    def is_overlap(self, A, B, C, D, E, F, G, H):
        if C <= E or G <= A or H <= B or D <= F:
            return False

        return True

    def area(self, p1, p2, p3, p4):
        return (p3 - p1) * (p4 - p2)

        math.sqrt()
