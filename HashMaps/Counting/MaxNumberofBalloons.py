class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        bDict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for i in range (0, len(text)):
            if text[i] in bDict:
                bDict[text[i]] += 1
            
        
        occurrences = []
        
        for key in bDict:
            if key == 'l' or key == 'o':
                occurrences.append(bDict[key]//2)
            else:
                occurrences.append(bDict[key])
        
        return min(occurrences)
        