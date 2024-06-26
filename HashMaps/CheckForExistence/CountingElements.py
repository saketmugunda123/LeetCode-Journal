class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        answerSet = set(arr)
        count = 0
        
        for i in range (0, len(arr)):
            if(arr[i] + 1 in answerSet):
                count +=1
        
        return count
                
        