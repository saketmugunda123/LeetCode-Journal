class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
  
        curr = ''
        stack = []
        
        for letter in path + '/':
            
            if letter == '/':
                if curr == '..':
                    if stack: stack.pop()
                elif curr != '' and curr != '.':
                    stack.append(curr)
                curr = ''
            else:
                curr += letter
            
            print(curr)
            
        return '/' + '/'.join(stack)
                    
            