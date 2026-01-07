"""2095. Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

link :https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

"""
"""Brute force approach 
* Count the len of list 
* Count the middle element
* Go to the element before middle element and link it to next element
* Go to the middle element and remove the link
"""
def deleteMiddle(head) :
        count = 0
        temp = head
        while(temp):
            temp = temp.next
            count+=1
        if count ==1:
            return None
        i = count//2
        count=1
        prev = head
        curr = head.next
        while(count<i):
            count+=1
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        curr.next = None
        return head

"""optimal approach : Slow and fast pointer approach"""
def deleteMiddle(head) :
    if not head.next:
            return head.next
    else: 
        slow = head
        fast = head.next.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head   