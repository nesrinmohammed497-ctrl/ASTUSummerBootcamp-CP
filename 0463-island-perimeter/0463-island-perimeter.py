class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        column=len(grid[0])
        p=0
        for i in range(row):
            for j in range(column):
                k=grid[i][j]
                if k==1 :
                    if i==0 or grid[i-1][j]==0  :
                        p+=1
                    if j==0 or grid[i][j-1]==0 :
                        p+=1
                    if i==row-1 or grid[i+1][j]==0:
                        p+=1
                    if j==column-1 or grid[i][j+1]==0 :
                        p+=1
        return p
        


        