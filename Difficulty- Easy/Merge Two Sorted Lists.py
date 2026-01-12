class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy=ListNode()
        current=dummy
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                current.next=l2
                l2=l2.next
            else:
                current.next=l1
                l1=l1.next
            current=current.next
        if l1:
            current.next=l1
        else:
            current.next=l2
        return dummy.next           
        
        