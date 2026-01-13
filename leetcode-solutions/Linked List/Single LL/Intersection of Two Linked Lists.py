"""160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
If you correctly return the intersected node, then your solution will be accepted.

Problem Link : https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """Start of solution"""
    starta = headA #Start of one head
    startb = headB #Start of other head
    s = set() #Set to store nodes
    if starta ==startb: # Edge case when the start are same
        return starta
    while starta: #Iterate through start and store it in set
        s.add(starta) #Add node to set
        starta = starta.next
    while startb: # Iterrate through other start
        if startb in s: # Check if the node is in Set
            return startb
        startb = startb.next
    
    return startb
"""Logic:
Storing each node in a set iterating form one head.
Iterate from other head and look for the value in set

Time complexity : O(m x n)
Space complexity : O(m)


"""