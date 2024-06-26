class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winnersDict = {}
        losersDict = {}
        
        for match in matches:
            winner = match[0]
            loser = match[1]
    
            if winner not in winnersDict:
                winnersDict[winner] = 1
                
            if loser not in losersDict:
                losersDict[loser] = 1
            else:
                losersDict[loser] +=1
            
        undefeated = []
        oneLoss = []
        for key in winnersDict:
            if key not in losersDict:
                undefeated.append(key)
        
        for key in losersDict:
            if losersDict[key] ==1:
                oneLoss.append(key)
        
        undefeated.sort()
        oneLoss.sort()
        
        answerList = [undefeated, oneLoss]
        
        return answerList
            
                