"""Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Problem Link :https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2) :
        temp_head = ListNode()
        temp = temp_head
        carry=0
        h1 = l1
        h2 = l2
        while(h1 or h2 or carry):
            res = 0
            if h1:
                res += h1.val
                h1 = h1.next
            if h2:
                res += h2.val
                h2 = h2.next
            
            res+=carry
            node = ListNode(res%10)
            
            carry = res //10
            temp.next = node
            temp = temp.next
        
        return temp_head.next
