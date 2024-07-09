class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        res = ''
        
        while temp_node is not None:
            res += str(temp_node.value)
            if temp_node.next is not None:
                res += '->'
            temp_node = temp_node.next
        return res
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        
    def insert(self, value, index):
        new_node = Node(value)
        
        if index < 0 or index > self.length:
            return False
        
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        
        self.length += 1
        return True
        
    def append(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
            
    def search(self, target):
        curr = self.head
        index = 0
        while curr:
            if curr.value == target:
                return index
            curr = curr.next
            index += 1
        return -1
        
    def get(self,index):
        curr = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            curr = curr.next
        return curr
        
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
        
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -=1
        return popped_node
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:   
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
            
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
nll = LL()
nll.append(10)
nll.append(20)
nll.append(30)
#nll.pop_first()
print(nll.remove(1))
print(nll)
        
