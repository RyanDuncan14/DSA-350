import pandas as pd 
import random 


class Student: 
    def __init__(self, first, last):
        self.first = first 
        self.last = last 
        self.sid = random.randint(1000,9999)
    
    def __str__(self):
        return self.first + " " + self.last + " ID: " + str(self.sid)


class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None
        
if __name__ == '__main__':
    s1 = Student("jobs", "steve")
    s2 = Student("gary", "man")
    s3 = Student("billy", "bob")
    
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.size = 0 
        
    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.size -= 1 
        return current_head
    
    def add(self,item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        self.size += 1

    def is_empty(self):
        if self.head is None:
            return False
        else:
            return True  
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
       
        return_str = "Queue object: "
        for node in self:
            return_str = return_str + str(node.data) + "--"
            return return_str
        
        def __str__(self):
            if self.is_empty():
                return "Waitlist: Empty"

            return_str = "Waitlist:  "
            first_node = True
            for node in self:
                if not first_node:
                    return_str += " -- "
                return_str += node.data.first + " " + node.data.last
                first_node = False
            return return_str


if __name__ == '__main__':
    s1 = Student("jobs", "steve")
    s2 = Student("gary", "man")
    s3 = Student("billy", "bob")

    waitlist = Queue()
    waitlist.add(s1)
    waitlist.add(s2)
    waitlist.add(s3)

    print(waitlist)
    print("size is: ", waitlist.size)

    while not waitlist.is_empty():
        waitlist.pop_left()
        print(waitlist)
        if not waitlist.is_empty():
            print("size is: ", waitlist.size)