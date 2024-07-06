# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head 
        fast = head
        
        while fast != None and fast.next != None: #Order of conditions matter bc 
                                                   #Compiler can possibly check a none.next which isn't possible
            slow = slow.next
            fast = fast.next.next
        
        
        return slow
        
        