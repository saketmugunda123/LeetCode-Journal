class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()
        answer = []
        for word in words:
            i = 0
            j = len(word) -1
            tempAnswer = []
            while(j >= i):
                tempAnswer.append(word[j])
                j -=1
            reversedWord = ''.join(tempAnswer)
            answer.append(reversedWord)

        return ' '.join(answer)


