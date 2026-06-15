# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # use turtle and hare again

        slow = fast = head
        dummy = ListNode(0, head)
        prev = dummy

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next

        return dummy.next


        

        
