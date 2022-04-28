## Given the head of a linked list, return the list after sorting it in ascending order.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    """use merge sort"""
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge(l1.next, l2)
        
        return l1 or l2
        
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head 
    
        half,slow, fast = None, head, head 
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None 

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.merge(l1, l2)

# runtime: 788ms / memory 54.2MB

######
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        """use python basic function"""
        ## linked list -> python list
        curr = head 
        l = []

        while curr:
            l.append(curr.val)
            curr = curr.next 

        l.sort()

        ## python list - linked list 
        curr = head 
        for i in range(len(l)):
            curr.val = l[i]
            curr = curr.next 
        
        return head 

# runtime: 220ms / memory: 30.1MB 