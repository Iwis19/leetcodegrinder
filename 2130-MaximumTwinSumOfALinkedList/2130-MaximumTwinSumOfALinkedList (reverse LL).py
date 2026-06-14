# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        """
        after submitting my array solution, i wanted to see the suggested sol.

        i read the description, honestly did think about turtle and hare to get to the middle array (respect)
        but had a hard time implementing reverse since i kept mixing up different assignments.

        62 ms runtime beats 50% dont like this implementation but its a good refresher on reversing.
        """
        
        slow = fast = head
        prev = None

        # turtle and hare thingie
        while fast and fast.next:

            fast = fast.next.next

            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

            # swapping logic!!!!!!!!!!!!!!!!!!! watch out on swapping, its pretty tricky, also the order as well. it doesnt just staright up get
            # the existing RHS and plug it into LHS, order still matters. it uses temp vars under disguise.

        res = -1
        while slow:
            twin_sum = prev.val + slow.val
            if twin_sum > res:
                res = twin_sum
            prev, slow = prev.next, slow.next

        return res

