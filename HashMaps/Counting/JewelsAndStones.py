class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        jewelsDict = {}
        
        for i in range(0, len(jewels)):
            if jewels[i] not in jewelsDict:
                jewelsDict[jewels[i]] = 1
            else:
                jewelsDict[jewels[i]] += 1
        
        count = 0
        for stone in stones:
            if stone in jewelsDict:
                count +=1
            
        return count

                
        