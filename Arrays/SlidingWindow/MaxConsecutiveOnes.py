class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        answer = 0
        originalK = k
        currSum = 0
        
        for right in range (0, len(nums)):
            
            currSum += nums[right]
            
            while(right-left  + 1 > currSum + k):
                currSum -= nums[left]
                left+=1
                
            answer = max(answer,right-left+1)
            
        return answer
    
    #time complexity O(n) 
    #space compleixty O(1)

        