class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsDict = {}
        for i in range(0, len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] +=1
        
        sum = 0
        for key in numsDict:
            if numsDict[key] == 1: 
                sum += key
        return sum

        