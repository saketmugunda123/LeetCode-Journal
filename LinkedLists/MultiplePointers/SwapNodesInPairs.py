# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            #Storing the next pair
            nextPair = curr.next.next

            #second node in pair (curr represents the first)
            second = curr.next

            #reverse the nodes
            second.next = curr
            curr.next = nextPair
            prev.next = second

            #update curr and prev
            prev = curr #prev is always one behind curr initally (in the last pair)
            curr = nextPair   
        
        return dummy.next #Dummy.next is the first node in this new linked list
        