class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.val)
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        res = ''
        while temp_node is not None:
            res += str(temp_node.val)
            if temp_node.next is not None:
                res += ' <-> '
            temp_node = temp_node.next
        return res
        
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def prepend(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
        
    def reverse_traverse(self):
        curr = self.tail
        while curr:
            print(curr.val)
            curr = curr.prev
            
    def search(self,target):
        curr = self.head
        index = 0
        while curr:
            if curr.val == target:
                return index
            curr = curr.next
            index += 1
        return -1
        
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length-1, index, -1):
                curr = curr.prev
        return curr
        
    def set_value(self,val,index):
        temp = self.get(index)
        if temp:
            temp.val = val
            return True
        return False
        
    def insert(self,val,index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.prepend(val)
        elif index == self.length:
            return self.append(val)
        else:
            new_node = Node(val)
            temp_node = self.get(index-1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
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
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
        
    def remove(self,index):
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
            popped_node.next.prev = prev_node
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
        
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(30)
dll.prepend(50)
dll.append(60)
print(dll)
dll.remove(4)
print(dll)
        
