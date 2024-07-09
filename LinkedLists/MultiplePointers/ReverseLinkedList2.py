# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        dummy = ListNode(0, head)
        
        prev = dummy
        curr = head
        pos =1
        while pos != left:
            prev = curr
            curr = curr.next
            pos +=1
        
        leftBound = curr
   
        nxtNode = curr.next
        pos +=1
        while pos <= right:
            #store next node
            nxtNode2 = nxtNode.next
    
            nxtNode.next = curr 
            curr = nxtNode
            nxtNode = nxtNode2
            pos +=1
        
        
        
        prev.next = curr
        leftBound.next = nxtNode
    
       
        
        return dummy.next
        
            
            
        
        
            
        
        
        
        
            