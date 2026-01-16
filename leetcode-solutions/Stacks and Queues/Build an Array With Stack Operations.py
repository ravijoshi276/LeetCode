"""Q1. Build an Array With Stack Operations

You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

"Push": pushes an integer to the top of the stack.
"Pop": removes the integer on the top of the stack.
You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
If the stack is not empty, pop the integer at the top of the stack.
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

 

Problem Link : https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
"""


def buildArray(target, n: int):
    target_index = 0 # Stores index of target
    output = []
    target_len = len(target) # End of target
    for i in range(1,n+1):
        if target_index < target_len and i == target[target_index]:
            if target_index > 0: # Case where we alredy pushed first element in target
                pointer = i
                while(pointer>target[target_index-1]+1): # Loop from pointer to target and pop all the elements till value
                    output.append("Pop")
                    pointer-=1

            else: # Case where our target is still empty 
                pointer = 1
                while(pointer<target[target_index]): # Loop till value of the target element and remove all the elements
                    output.append("Pop")
                    pointer+=1
            output.append("Push")
            target_index +=1
            
        else: # if the value dosent match the target
            output.append("Push")
        if target_index == target_len:
            break
        
    return output

"""We have and interger array 
Case 1 : where we still havent found the first element or target array.
    * We push till we find the target
    * As soon as we find the target . We loop till target and pop all the elements pushed in stack.
    * Then push the target in stack
    * move the pointer on the target to next
Case 2 : Where we have pushed the first element.
    * We push till we find the target
    * As soon as we find the target.
    * We put a pointer to the element and loop backwards and pop the items till the last inserted value.
    
"""