class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tempSum = 0
        Pnums = []
        for i in range(0, len(nums)):
            tempSum +=nums[i]
            Pnums.append(tempSum)
            
        answer = 1 -min(Pnums)
        
        if answer <= 0:
            return 1
        
        return answer