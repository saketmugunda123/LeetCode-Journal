class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackS = []
        for letter in s:
            if letter != '#':
                stackS.append(letter)
            else:
                if stackS:
                    stackS.pop()
        
        stackT = []
        for letter in t:
            if letter != '#':
                stackT.append(letter)
            else:
                if stackT:
                    stackT.pop()
    
        
        ''.join(stackS)
        ''.join(stackT)

        if stackS != stackT:
            return False
        return True
