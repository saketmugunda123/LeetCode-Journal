class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        rNums = [0]*len(nums)
        
        leftPointer = 0
        rightPointer = len(nums)-1
        position = len(nums) -1
        
        while (position >= 0):
            leftSquare = nums[leftPointer]**2
            rightSquare = nums[rightPointer]**2
            if(leftSquare >= rightSquare):
                rNums[position] = leftSquare
                leftPointer +=1
                
            elif(rightSquare > leftSquare):
                rNums[position] = rightSquare
                rightPointer -=1
            
            position -=1
            
        return rNums
                



            
            