class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms or len(rooms) == 0 or len(rooms[0]) == 0:
            return

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, d):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] < d:
            return

        rooms[i][j] = d

        self.dfs(rooms, i-1, j, d+1)
        self.dfs(rooms, i+1, j, d+1)
        self.dfs(rooms, i, j-1, d+1)
        self.dfs(rooms, i, j+1, d+1)