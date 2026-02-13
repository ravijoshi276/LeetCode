""" Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Problem link : https://leetcode.com/problems/implement-queue-using-stacks/
"""

"""
Logic : Keep track of start, end and length of stack[list]
* Elements are added to the end pointer
* Element are removed from the start
* After removing the element from the start it is set to null and start is set to next element
* The length tracks the length. If there is space available in the stack it will be used first and then a new element will be introduced.
"""
#Test Cases
"""
["MyQueue","empty","push","push","empty","peek","push","push","peek","pop","empty","peek","pop","empty"]
[[],[],[1],[1],[],[],[5],[5],[],[],[],[],[],[]]
["MyQueue","push","pop","push","empty","push","pop","peek","push","empty","pop","pop","push","push","peek","empty","empty","empty","pop","pop","push","push","pop","empty","empty","pop","push","empty","push","pop","push","peek","empty","pop","peek","push","empty","push","empty","push","peek","pop","empty","empty","pop","push","pop","pop","empty","push","pop","push","push","empty","empty","empty","peek","peek","peek","empty","pop","empty","pop","push","empty","pop","pop","push","empty","push","pop","empty","pop","push","peek","pop","push","push","push","push","empty","pop","peek","pop","pop","push","peek","pop","pop","push","pop","push","peek","push","empty","push","empty","push","peek","pop","pop"]
[[],[7],[],[8],[],[4],[],[],[4],[],[],[],[5],[7],[],[],[],[],[],[],[9],[8],[],[],[],[],[9],[],[4],[],[5],[],[],[],[],[6],[],[7],[],[5],[],[],[],[],[],[5],[],[],[],[2],[],[7],[5],[],[],[],[],[],[],[],[],[],[],[2],[],[],[],[8],[],[2],[],[],[],[2],[],[],[1],[7],[9],[5],[],[],[],[],[],[8],[],[],[],[7],[],[6],[],[7],[],[4],[],[2],[],[],[]]
["MyQueue","push","push","push","push","push","peek","push","push","push","push","peek","pop","pop","pop","pop","peek","pop","pop","peek","pop"]
[[],[1],[4],[9],[2],[2],[],[1],[2],[7],[1],[],[],[],[],[],[],[],[],[],[]]
["MyQueue","push","push","push","push","push","push","push","push","push","push","peek","pop","pop","pop","pop","pop","pop","pop","peek","pop"]
[[],[5],[6],[7],[6],[1],[8],[2],[5],[4],[7],[],[],[],[],[],[],[],[],[],[]]
["MyQueue","push","push","push","push","push","push","push","push","push","push","peek","pop","pop","pop","pop","pop","pop","empty","peek","pop"]
[[],[4],[5],[6],[7],[8],[1],[1],[2],[3],[4],[],[],[],[],[],[],[],[],[],[]]
["MyQueue","empty","push","push","push","push","push","empty","push","push","push","peek","empty","peek","pop","pop","empty","pop","pop","peek","pop"]
[[],[],[1],[1],[1],[1],[1],[],[3],[4],[5],[],[],[],[],[],[],[],[],[],[]]
["MyQueue","push","pop","empty","push","pop","push","pop","push","peek","empty","pop","push","pop","push","peek","pop","empty","push","pop","push"]
[[],[1],[],[],[2],[],[3],[],[4],[],[],[],[5],[],[6],[],[],[],[7],[],[8]]
["MyQueue","push","push","peek","pop","push","empty","pop","pop","push","push","empty","push","empty","pop","pop","peek","peek","peek","empty","empty","push","pop","pop","push","peek","pop","push","empty","pop","push","empty","empty","pop","push","empty","pop","push","empty","pop","push","peek","push","empty","pop","empty","pop","push","pop","push","empty","pop","push","empty","pop","push","pop","push","peek","pop","push","empty","pop","push","pop","push","push","empty","push","push","pop","empty","pop","push","pop","peek","pop","pop","push","peek","peek","push","empty","push","push","empty","empty","peek","empty","push","pop","pop","pop","peek","empty","pop","push","peek","empty","empty","peek"]
[[],[9],[3],[],[],[5],[],[],[],[3],[8],[],[8],[],[],[],[],[],[],[],[],[4],[],[],[4],[],[],[8],[],[],[3],[],[],[],[4],[],[],[8],[],[],[2],[],[6],[],[],[],[],[1],[],[7],[],[],[8],[],[],[5],[],[6],[],[],[3],[],[],[9],[],[2],[6],[],[3],[5],[],[],[],[6],[],[],[],[],[9],[],[],[2],[],[3],[4],[],[],[],[],[3],[],[],[],[],[],[],[1],[],[],[],[]]

"""

class MyQueue:

    def __init__(self):
        self.q =[]
        self.start=0
        self.end=0
        self.length =0
    def push(self, x: int) -> None:
        
        n = len(self.q)

        if n==0:
            self.end=0
            self.q.append(x)
            
        elif self.length == n:
            if self.end == n-1:
                self.q.append(x)
                self.end +=1
            else:
                self.end+=1
                self.q.insert(self.end,x)
                self.start = self.start+1
        elif self.length < n :
            self.end = (self.end +1) % n
            self.q[self.end] = x
            
    
        self.length +=1
    def pop(self) -> int:
        temp = None
        n = len(self.q)
        if self.length ==0:
            return temp
        else :
            temp = self.q[self.start]
            self.q[self.start]= None
            self.start = (self.start +1) % n
            self.length -=1
        if self.length ==0:
            self.q =[]
            self.start,self.end =0,0
        return temp
    def peek(self) -> int:
        if self.length != 0:
            return self.q[self.start]
        else:
            return None
    def empty(self) -> bool:
        if self.length ==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()