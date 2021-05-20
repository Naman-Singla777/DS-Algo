class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        tail = temp
        
        while l1 or l2:
            try:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                elif l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            except:
        
                if l1:
                    tail.next = l1
                elif l2:
                    tail.next = l2
            
        return temp.next
