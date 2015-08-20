# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def makeList(cls, l):
        head = None
        curr = head
        for n in l:
            if curr:
                curr.next = ListNode(n)
                curr = curr.next
            else:
                head = ListNode(n)
                curr = head
        return head

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = None
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next

            if curr:
                curr.next = node
                curr = curr.next
            else:
                head = node
                curr = head
        
        node = None
        if l1:
            node = l1
        elif l2:
            node = l2
        if curr:
            curr.next = node
        else:
            head = node
    
        return head
            

solu = Solution()
l1 = [5]
l2 = [1,2,4]
ret = solu.mergeTwoLists(ListNode.makeList(l1), ListNode.makeList(l2))
