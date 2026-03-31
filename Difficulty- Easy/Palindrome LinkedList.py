class Solution:
    def isPalindrome(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            slow.next,prev,slow=prev,slow,slow.next
        while prev:
            if head.val!=prev.val:
                return False
            head,prev=head.next,prev.next
        return True
