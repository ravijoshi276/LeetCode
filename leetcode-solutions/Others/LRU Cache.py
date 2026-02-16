"""LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Problem Link : https://leetcode.com/problems/lru-cache/description/
"""
"""
Logic : 
* A double linked list for storing the cache.
* A hash map for storing the key along with the Node

deleteNode(Node) : deletes the link to node
addNode(Node) : Adds the node next to head (adding it to most recently used queue)
get(key) : Returns the value of key if exist and also updates it in LRU cache
put(key,value) : checks if cache memory is full and then does the necessary 

"""
class LRUCache:
    class Node:
        def __init__(self,key,val,next=None,prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev
    
    def __init__(self, capacity: int):
        #Capacity of cache
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        #hash map to store key node mapping 
        self.mpp = {}
    def addNode(self,newnode):
        temp = self.head.next
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = temp
        temp.prev = newnode

    def delNode(self,deleteNode):
        prev = deleteNode.prev
        next = deleteNode.next
        prev.next = next
        next.prev = prev
        deleteNode.prev = None
        deleteNode.next = None

    def get(self, key: int) -> int:
        if key in self.mpp:
            resNode = self.mpp[key]
            res = resNode.val
            
            # deleting key from map
            del self.mpp[key]
            # Deleting Node from linked list 
            self.delNode(resNode)
            self.addNode(resNode)

            #storing key
            self.mpp[key] = self.head.next            

            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mpp:
            existingNode = self.mpp[key]
            self.delNode(existingNode)
            del self.mpp[key]
        if len(self.mpp) == self.capacity:
            del self.mpp[self.tail.prev.key]
            self.delNode(self.tail.prev)
        self.addNode(self.Node(key,value))
        self.mpp[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)