class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        answer = 0
        
        #Increment 1 if 1 appears and decrement 1 if 0 appears
        #Store count values in dictionary
        
        countDict = {}
        
        for i in range(0,len(nums)):
            if(nums[i] == 1):
                count +=1
            else:
                count -=1
                
            if count == 0:
                answer = max(answer, i + 1)
                continue
                
            if count in countDict:
                answer = max(answer, i - (countDict[count] + 1) +1)
            else:
                countDict[count] = i
            
        
        return answer
                
            