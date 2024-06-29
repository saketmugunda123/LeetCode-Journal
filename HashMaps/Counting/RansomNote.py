class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magDict = {}
        
        for i in range(0, len(magazine)):
            if magazine[i] not in magDict:
                magDict[magazine[i]] = 1
            else:
                magDict[magazine[i]] +=1
        
        for j in range(0, len(ransomNote)):    
            if ransomNote[j] not in magDict:
                return False
    
            magDict[ransomNote[j]] -= 1
            
            if magDict[ransomNote[j]] < 0:
                return False
        
        return True
        
        
        
        
        