
"""Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Problem link : https://leetcode.com/problems/min-stack/"""
class MinStack:
    class Node:
        def __init__(self,val=None,prev=None,next=None):
            self.val=val
            self.next=next
            self.prev=prev
            

    def __init__(self):
        self.head= self.Node(-1)
        self.tail = self.Node(-1)
        self.head.next = self.tail
        self.tail.prev= self.head
        self.minimum = None
        self.length =0
      
             

    def push(self, val: int) -> None:
        
        new_node = self.Node()
        if self.length ==0:
            new_node = self.Node(val)
            temp = self.tail.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.tail
            self.tail.prev= new_node
            self.minimum = val
        else:
            if val > self.minimum:
                new_node = self.Node(val)
                temp = self.tail.prev
                temp.next = new_node
                new_node.prev = temp
                new_node.next = self.tail
                self.tail.prev= new_node
            else:
                prev_val = val
                prev_minimum = self.minimum
                self.minimum = prev_val
                val = 2 *val -prev_minimum
                new_node = self.Node(val)
                temp = self.tail.prev
                temp.next = new_node
                new_node.prev = temp
                new_node.next = self.tail
                self.tail.prev= new_node
              
        self.length+=1
    
    def pop(self) -> None:
        
        if self.length ==0:
            return None
        self.length -=1
        res = self.tail.prev.val
        new_top = self.tail.prev.prev
        new_top.next= self.tail
        self.tail.prev= new_top
        if res is None:
            return res
        elif res < self.minimum:
            temp= self.minimum
            self.minimum = 2 *self.minimum - res
            
        
    def top(self) -> int:
        
        if self.length ==0:
            return None
        else:
            temp = self.tail.prev.val
            if temp < self.minimum:
                return self.minimum
            
            return temp

    def getMin(self) -> int:
       
        if self.length ==0 or self.minimum is None:
            return None
        else:
            res = self.minimum
            
           
           
        return res


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()