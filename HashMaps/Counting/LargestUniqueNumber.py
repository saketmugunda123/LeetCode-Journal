class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numsDict = {}
        
        for i in range (0, len(nums)):
            if(nums[i] not in numsDict):
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] +=1
              
        answerList = []
        
        for key in numsDict:
            if(numsDict[key] == 1):
                answerList.append(key)
        
        if len(answerList) == 0:
            return -1 
        
        answer = max(answerList)
        
        return answer
                