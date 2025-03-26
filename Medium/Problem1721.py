# Return head of a linked list after swapping kth index from the beginning with kth index from the end (1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        a = b = head
        for j in range(k-1):
            a=a.next
        left=a
        while a.next is not None:
            a = a.next
            b = b.next
        left.val, b.val = b.val, left.val
        return head