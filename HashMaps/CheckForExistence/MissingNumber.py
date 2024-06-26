class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        
        total = (length* (length + 1))/2
        
        for num in nums:
            total -= num
        
        return total
        