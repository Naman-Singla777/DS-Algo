class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # dummy = ListNode(0)
        # tail = dummy
        temp = head
         
        l = 0
        
        while head:
            l+=1
            head = head.next
            
        if l == n:
            return temp.next
      
        
        # if l == 2 and n == 1:
        #     temp.next = None
        #     return temp
            
        t = l - n - 1
        
        c = 0
        head = temp
        while c<t:
            c+=1
            # if c != t:
            #     tail.next = temp
            #     tail = tail.next
            temp = temp.next
            
        temp.next = temp.next.next
                    
        return head
