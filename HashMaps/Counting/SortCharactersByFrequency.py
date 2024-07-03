class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        sDict = {}
        for i in range(0, len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] +=1
        
    
        newDict = {}

        for key in sDict:
            newDict[(sDict[key], key)] = key
        
        newDict = sorted(newDict)


        answerString = ''
        for key in newDict:
            answerString += key[0]*key[1]
        
        newString = answerString[::-1]
        return newString
        