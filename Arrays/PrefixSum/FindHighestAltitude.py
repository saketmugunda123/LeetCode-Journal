class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
    
        altitudesList = [0]
        tempSum = 0
        for i in range (0, len(gain)):
            tempSum += gain[i]
            altitudesList.append(tempSum)
        
        return max(altitudesList)
        