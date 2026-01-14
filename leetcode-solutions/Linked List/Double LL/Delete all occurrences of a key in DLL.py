"""Delete all occurrences of a key in DLL

Given the head of a doubly linked list and an integer target. 
Delete all nodes in the linked list with the value target and return the head of the modified linked list

Problem Link :https://takeuforward.org/plus/dsa/problems/delete-all-occurrences-of-a-key-in-dll?tab=description
"""


# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev


def deleteAllOccurrences(head, target):
    curr = head #Current
    prev = head #previous
    nxt = head # Next
    
    while curr :
        if curr.val == target: #Case 1
            if not curr.prev:
                nxt = curr.next
                curr.next = None
                nxt.prev = None
                curr = nxt
                head = curr
            elif curr.next: # Normal Case
                prev = curr.prev
                nxt = curr.next
                prev.next = nxt
                nxt.prev = prev
                curr.next = None
                curr.prev = None
                curr = nxt
            else: #Case 3
                prev = curr.prev
                prev.next = None
                curr.prev = None
                curr= curr.next


        else: #If value didnt match target
            curr = curr.next
    
    return head

"""Logic:
1. Take 3 pointer which points to previous,next and current element
2. Make link of previsous to next element and remove the link of current element from both previous and next.
Edge Cases :
    1. When the first element if target.
    Solution : Point previous element to current and then move current to next. Break link of previos and 
    break link of current element to the previous element and also update the head to current. 
    2. When last element is target.
    Solution : Take previous as previous element break its link to current element and also break
    Link of current element to previous element. Move current element to next which becomes null and loop breaks
    
"""