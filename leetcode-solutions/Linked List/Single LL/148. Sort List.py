"""148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.


Problem link :https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head) :
        #Start of solution
        def findmiddle(head): # --> A function to find middle element
            slow = head
            fast = head.next

            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next
            return slow
        
        
        def merge(list1,list2): # --> Merging the linked list

            temp_head = ListNode(-1)

            temp = temp_head

            while list1 and list2:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next
            if list1:
                temp.next = list1
            else:
                temp.next = list2
            
            return temp_head.next

        if not head or not head.next: # checking if the head exist
            return head
        
        
        #Finding middle
        middle = findmiddle(head)

        # Left and right head
        left_head = head # Left pointer
        right_head = middle.next # right pointed
        middle.next = None # Breaking the link

        #Calling algorithm to break it down

        left_head = self.sortList(left_head)
        right_head = self.sortList(right_head)
        merged =  merge(left_head,right_head)

        return merged
"""
Logic :

The solution is a merge sort algorithm.
We find the middle of linked list.
We breat the list from the middle till the length of elements is 1
We merge them and retuen the head
"""