class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.list = []:
            return True
        else:
            return False
            
    def push(self,value):
        self.list.append(value)
        return "The element is pushed into the stack"
        
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            self.list.pop()
            
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]
            
    def delete(self):
        self.list = None
        
        
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.pop()
st.peek()
st.isEmpty()

