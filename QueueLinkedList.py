class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextt = None
    
    def __str__(self):
        return str(self.val)
    
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
class Queue:
    def __init__(self):
        self.linkedlist = LL()
        
    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,val):
        new_node = Node(val)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node
    
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return popped_node
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.linkedlist.head
    
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        
cq = Queue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq)
cq.dequeue()
print(cq)
print(cq.peek())
