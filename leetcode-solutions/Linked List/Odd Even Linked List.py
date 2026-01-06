"""328. Odd Even Linked List


Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Link :https://leetcode.com/problems/odd-even-linked-list/description/


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
def oddEvenList(head) :
        if head is None:  #--> Case when list is empty
            return head
        odd = head # will store odd list
        even_head = head.next # even head to link
        even = head.next # even list
        while(odd.next and even.next): # While there is next
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even= even.next
        odd.next = even_head # Attach even head to odd tail
        try :
            even.next = None # if the linked list is even size even. next will already be none. It can throw error
        finally :
            return head
"""

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Logic : Simply go through list. 
        Link all even position
        Link all odd position
        and link the head of even to tail of odd
        make the end of linked list None if not none
"""