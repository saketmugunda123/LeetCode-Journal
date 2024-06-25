class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #Get prefix sum
        tempSum = 0
        Pnums = []
        for p in range (0, len(nums)):
            tempSum += nums[p]
            Pnums.append(tempSum)
            
        answerList = []
        for i in range (0, len(nums)):
            if((i - k < 0) or (i + k >= len(nums))):
                answerList.append(-1)
                continue

            currSum = Pnums[i+k] - Pnums[i-k] + nums[i-k]
            avg = currSum // (2*k + 1)
            answerList.append(avg)
        
        return answerList