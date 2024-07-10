# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #Get length of the linked list
        length = 0
        start = head
        while start:
            start = start.next
            length +=1
        
        if length == 1 or length == 2:
            return head

        #Check to see how much is left over
        num = 1
        numsList = []
        while True:
            if length - num <= 0:
                break
            length -= num
            numsList.append(num)
            num +=1 
        numsList.append(length)
        print(numsList)
        
        #Determine whether or not last group needs to be reversed and number of iterations
        #Reverse what is needed
        dummy = ListNode(0, head)
        prev = dummy
        curr = head 

        for i in range (0, len(numsList)):
            counter = 0
            if numsList[i] % 2 == 1:
                while counter < numsList[i]:
                    prev = curr
                    curr = curr.next
                    counter +=1
            else:
                leftBound = prev
                prev = curr
                right = prev
                curr = curr.next
                while counter < numsList[i] -1:
                    nxtNode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxtNode
                    counter +=1
                leftBound.next = prev
                prev = right
                right.next = curr
                
            
        return dummy.next
