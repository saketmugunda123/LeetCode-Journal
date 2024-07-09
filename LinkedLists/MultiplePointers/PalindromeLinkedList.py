# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(0,head)
        prevOrig = dummy
        slow = head
        fast = head
        start = head
        

        while fast != None and fast.next != None:
            prevOrig
            slow = slow.next
            fast = fast.next.next
        

        #reverse the second half of the list
        prev = None
        while slow != None:
            nxtNode = slow.next
            slow.next = prev
            prev = slow
            slow = nxtNode
        
        end = prev
        while end != None:
            if end.val != start.val:
                return False
            end = end.next
            start = start.next
    
        return True
        
        



        
        
