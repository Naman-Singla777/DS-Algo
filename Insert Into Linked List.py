class Solution:
    def solve(self, head, pos, val):
        ans = head
        ins = LLNode(val)
        if pos == 0:
            ins.next = head
            return ins
        c = 0
        while head:
            c+=1
            if c == pos:
                ins.next = head.next
                head.next = ins
            head = head.next
        return ans
     
