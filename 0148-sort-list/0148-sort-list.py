# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current=head
        count=[]
        while current!=None:
            count.append(current.val)
            current=current.next 
        count=sorted(count)
        print(count)
        current=head
        for i in range(len(count)):
            current.val=count[i]
            current=current.next  
        return head

        