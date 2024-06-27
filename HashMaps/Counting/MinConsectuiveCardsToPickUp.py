class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """

        cardsDict = {}
        answer = 1000000
        for i in range (0, len(cards)):
            if cards[i] not in cardsDict:
                cardsDict[cards[i]] = i
            else:
                answer = min(answer, i - cardsDict[cards[i]] + 1) 
                cardsDict[cards[i]] = i        
        
        if answer == 1000000:
            return -1
        return answer