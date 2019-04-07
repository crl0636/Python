class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        # do intialization if necessary
        self.i = 0
        self.v = []
        size = max(len(v1), len(v2))
        for i in range(size):
            if i < len(v1):
                self.v.append(v1[i])

            if i < len(v2):
                self.v.append(v2[i])

    """
    @return: An integer
    """
    def next(self):
        val = self.v[self.i]
        # write your code here
        self.i += 1
        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return self.i < len(self.v)

if __name__ == '__main__':
    so = ZigzagIterator([1,2], [3,4,5,6])
    res = []
    while (so.hasNext()):
        res.append(so.next())

    print res