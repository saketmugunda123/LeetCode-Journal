class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(s[0])
        for i in range (1,len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            curr = stack.pop()
            if curr == s[i]:
                continue
            else:
                stack.append(curr)
                stack.append(s[i])
        
        return ''.join(stack)

