class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        answer = set(sentence)
        if(len(answer) == 26):
            return True
        else:
            return False
        
        #O(1) Time Complexity
        #O(n) space complexity