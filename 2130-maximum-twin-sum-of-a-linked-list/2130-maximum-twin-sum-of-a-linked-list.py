# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        second_half_head = prev
        first_half_head = head
        max_val = 0
        
        while second_half_head:
            twin_sum = first_half_head.val + second_half_head.val
            max_val = max(max_val, twin_sum)
            
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next
            
        return max_val