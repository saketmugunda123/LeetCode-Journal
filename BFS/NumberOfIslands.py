class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
         if not grid:
            return 0
        
        #create the BFS function
        def BFS(row, col):
            queue = [(row,col)]
            grid[row][col] = '0' #marking node as visited
            while queue:
                currRow, currCol = queue.pop(0)
                directions = [(1,0), (-1,0),(0,1), (0,-1)] #getting neighbors
                for rowDirect, colDirect in directions:
                    newRow, newCol = currRow + rowDirect, currCol + colDirect
                    if(newRow >= 0 and newRow < len(grid) and newCol >=0 and newCol < len(grid[0]) and grid[newRow][newCol] == '1'):
                        queue.append((newRow,newCol)) #valid neighbor
                        grid[newRow][newCol] = '0' #mark as visited
        
        islandCount = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == '1':
                    BFS(r, c)
                    islandCount +=1
        
        return islandCount
                    