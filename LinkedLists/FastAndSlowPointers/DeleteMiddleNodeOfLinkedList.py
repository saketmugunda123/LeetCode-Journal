# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        prev = dummy
        fast = head
        middle = head
        

        while fast != None and fast.next != None:
            prev = middle
            middle = middle.next
            fast = fast.next.next
        
        prev.next = middle.next
        return dummy.next
        
        slow

        