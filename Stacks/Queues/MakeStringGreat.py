class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
       
        
        stack = [s[0]]
        for i in range (1, len(s)):
            if stack:
                if stack[-1].islower():

                    if stack[-1].upper() == s[i]:
                        stack.pop()
                        continue
                else:
                    if stack[-1].lower() == s[i]:
                        stack.pop() 
                        continue
            
            stack.append(s[i])
            
        return ''.join(stack)