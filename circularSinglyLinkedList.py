class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class CSLL:
    # def __init__(self,val):
    #     new_node = Node(val)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        res = ''
        while temp_node is not None:
            res += str(temp_node.val)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            res += '->'
        return res
        
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def prepend(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insert(self,val,index):
        if index < 0 or index > self.length:
            return None
        new_node = Node(val)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
            
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
            if curr == self.head:
                break
    
    def search(self,target):
        curr = self.head
        index = 0
        while curr:
            if curr.val == target:
                return index
            curr = curr.next
            index += 1
            if curr == self.head:
                break
        return -1
        
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr
    
    def set_value(self,val,index):
        temp = self.get(index)
        if temp:
            temp.val = val
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
            self.tail.next = self.head
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
            temp.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
        
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
    
    
csl = CSLL()
csl.append(10)
csl.append(20)
print(csl.search(1))
