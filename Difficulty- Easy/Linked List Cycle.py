class Solution:
    def hasCycle(self,head):
        one=two=head
        while two and two.next:
            one=one.next
            two=two.next.next
            if one==two:
                return True
        return False    
        