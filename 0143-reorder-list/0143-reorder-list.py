# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        c=[]
        curr=head
        while curr!=None:
            c.append(curr.val)
            curr=curr.next
        i=0
        j=0 
        print(c)
        curr=head
        while j<len(c) :
            if j%2==0:
                curr.val=c[i]
            else:
                i+=1
                curr.val=c[len(c)-i]
            curr=curr.next
            j+=1
        return head            
