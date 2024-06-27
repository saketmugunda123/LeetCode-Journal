class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        countDict = {}
        
        for i in range(0, len(strs)):
            temp = ''.join(sorted(strs[i]))
            
            if temp not in countDict:
                countDict[temp] =[strs[i]]
            else:
                countDict[temp] += [strs[i]]
        
        answerList = []
        for key in countDict:
            answerList.append(countDict[key])
        
        return answerList



        