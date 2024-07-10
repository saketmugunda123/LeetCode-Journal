# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
    
        length = 0
        start = head
        while start:
            length +=1
            start = start.next

        start = head
        length = length -1
        answer = 0
        while start:
            if start.val == 1:
                answer += 2**length 
            
            start = start.next
            length -=1
        
        return answer