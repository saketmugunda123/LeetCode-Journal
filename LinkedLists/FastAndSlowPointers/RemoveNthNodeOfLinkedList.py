# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev = dummy
        left = head
        right = head
        distance = 0

        while distance != n:
            right = right.next
            distance +=1

        while right != None:
            prev = left
            left = left.next
            right = right.next

        prev.next = left.next

        return dummy.next  