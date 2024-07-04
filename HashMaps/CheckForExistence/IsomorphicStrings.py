class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i in range(len(s)):
            tempS = s[i]
            tempT = t[i]
            
            if tempS in s_to_t:
                if s_to_t[tempS] != tempT:
                    return False
            else:
                s_to_t[tempS] = tempT
            
            if tempT in t_to_s:
                if t_to_s[tempT] != tempS:
                    return False
            else:
                t_to_s[tempT] = tempS
        
        return True
