class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        j = len(s) -1
        i=0
        while(i <j):
            temp1 = s[i]
            temp2 = s[j]
            s[j] = temp1
            s[i] = temp2
            i +=1
            j -=1
        
            
        