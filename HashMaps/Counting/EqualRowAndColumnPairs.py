class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rowsDict = {}
        for row in grid:
            row = tuple(row)
            if row not in rowsDict:
                rowsDict[row] =1
            else:
                rowsDict[row] +=1
    
        columnDict = {}
        for i in range(0, len(grid)):
            temp = []
            for j in range(0, len(grid)):
                temp.append(grid[j][i])  
            temp = tuple(temp)
            if temp not in columnDict:
                    columnDict[temp] =1
            else:
                columnDict[temp] +=1

        #If you have 2 rows and 2 columns that are the exact same, there are 4 total combinations
        answer = 0
        for key in rowsDict:
            if key in columnDict:
                answer += rowsDict[key] * columnDict[key]

        return answer


