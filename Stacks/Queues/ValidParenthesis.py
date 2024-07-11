class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracketDict = {
            '{': '}',
            '(':')',
            '[':']'
        }

        if len(s) == 0:
            return True

        stack = []
        for letter in s:
            if letter not in bracketDict:
                if len(stack) == 0:
                    return False
                curr = stack.pop() 
                if bracketDict[curr] != letter:
                    return False
            else:
                stack.append(letter)
        
        if len(stack) > 0:
            return False

        return True
            