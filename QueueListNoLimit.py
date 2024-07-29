class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        return False
        
    def enqueue(self,data):
        self.items.append(data)
        return "The element is inserted in the end of queue"
        
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
    
cq = Queue()
cq.enqueue(1)
cq.enqueue(2)
print(cq)
