class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Time complexity of O(n) now
        numsDict = {}
        answer = -1
        for i in range (0, len(nums)):
            #Get the sum of the digits
            tempStr = str(nums[i])
            digitSum = 0
            for digit in tempStr:
                digitSum += int(digit)
            
            if digitSum not in numsDict:
                numsDict[digitSum] = nums[i]
            else:
                answer = max(answer, numsDict[digitSum] + nums[i])
                numsDict[digitSum] = max(numsDict[digitSum], nums[i])
        
        return answer

        #BELOW IS THE INEFFICIENT SOLUTION OF TIME COMPLEXITY NLOGN BC OF THE SORT

        # numsDict = {}

        # for i in range(0, len(nums)):

        #     #Get the sum of the digits
        #     tempStr = str(nums[i])
        #     digitSum = 0
        #     for digit in tempStr:
        #         digitSum += int(digit)

        #     if digitSum not in numsDict:
        #         numsDict[digitSum] = [nums[i]]
        #     else:
        #         numsDict[digitSum].append(nums[i])

        # answer = -1
        # for key in numsDict:
        #     if(len(numsDict[key])) >= 2:
        #         numsDict[key].sort()
        #         answer = max(answer, sum(numsDict[key][-2:]))
            
        # return answer



        


        