# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        idk why this solution is like 2 lines of code diff from a 10 ms solution but is 75 ms aslower????

        think leetcode is being slow again but at least i remembered turtle and hare :0

        85 ms runtime beats 67%
        """

        if not head.next:
            return None
        
        # use turtle and hare again

        slow = fast = head
        dummy = ListNode(0, head)
        prev = dummy

        while fast and fast.next:

            fast = fast.next.next
            prev, slow = prev.next, slow.next

        prev.next = slow.next

        return dummy.next


        

        
