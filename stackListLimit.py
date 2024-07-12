#Stack using list with size limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
            
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been pushed into the stack"
            
    def pop():
        if self.isEmpty():
            return "The stack is empty"
        else:
            self.list.pop()
            
    def peek():
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]
            
    def delete(self):
        self.list = None
        
st = Stack(4)
st.push(1)
st.push(2)
st.push(3)
print(st.peek())
print(st.pop())
print(st.isEmpty())
print(st.isFull())
