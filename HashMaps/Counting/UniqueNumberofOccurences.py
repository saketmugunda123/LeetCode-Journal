class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        numberDict = {}
        for num in arr:
            if num not in numberDict:
                numberDict[num] = 1
            else:
                numberDict[num] +=1
        
        values = numberDict.values()
        
        setValues = set(values)

        if len(setValues) == len(values):
            return True
        else:
            return False
        