class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        
        pathDict = {}

        for path in paths:
            for i in range(2):
                if path[i] not in pathDict:
                    if i == 0:
                        pathDict[path[i]] = 1
                    else:
                        pathDict[path[i]] = 0
                else:
                    if i == 0:
                        pathDict[path[i]] += 1
        
        for key in pathDict:
            if pathDict[key] == 0:
                return key