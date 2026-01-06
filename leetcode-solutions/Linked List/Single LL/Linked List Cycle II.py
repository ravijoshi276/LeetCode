"""142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

link : https://leetcode.com/problems/linked-list-cycle-ii/description/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
def detectCycle(head) :
        # Start of solution
        slow = head
        fast = head
        flag = 0
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = 1
                break
        
        if flag == 1:
            slow = head
            while(True):
                if fast ==slow:
                    return slow
                slow = slow.next
                fast= fast.next

            
        return None
"""
Logic : Fast and slow pointer
"""