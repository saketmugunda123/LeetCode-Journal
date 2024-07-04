class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 1
        left = 0
        numsDict = {}
        for right in range(0, len(nums)):
            
            if nums[right] not in numsDict:
                numsDict[nums[right]] = 1
            else:
                numsDict[nums[right]] += 1

            while numsDict[nums[right]] > k:
                numsDict[nums[left]] -= 1
                left +=1
            
            answer = max(answer, right -left + 1)

        return answer
        
