class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        left = 0
        currSum = sum(nums[0:k])
        answer = currSum
        
        for i in range (k,len(nums)):
            currSum  -= nums[left]
            currSum += nums[i]
            
            left +=1
            
            answer = max(answer, currSum)
            
        
        answer = answer/ float(k)
        return answer
    
    #Time Complexity = O(n) bc O(k) + O(n-k) = O(n)
    #Space Complexity = O(1) as only constant time variables were defined
    
    
            

        