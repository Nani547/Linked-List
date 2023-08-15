class Main:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        node = Main(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            self.head = node
            node.next = curr
    def length(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        return count
            
    def insert_at_middle(self,data,index):
        node = Main(data)
        if index<0 or index>=self.length():
            raise Exception("Error in index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
            
        else:
            count = 0
            curr = self.head
            curr1 = curr.next
            while curr:
                if count == index-1:
                    curr.next = node
                    node.next = curr1 
                    break
                else:
                    curr = curr.next
                    curr1 = curr1.next
                    count += 1
    
        
    def display(self):
        if self.head is None:
            self.head = Main(data)
        else:
            curr = self.head
            while curr:
                print(curr.data,end="-->")
                curr = curr.next
                
    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Main(data)
        else:
            curr = self.head
            while curr.next:
                curr  = curr.next
            curr.next = Main(data)
        return self.head
    
    def remove(self,index):
        if index<0 or index>=self.length():
            raise Exception("Error in index")
        
        if index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            curr = self.head
            while curr:
                if count == index-1:
                    curr.next = curr.next.next
                    break
                else:
                    curr = curr.next
                    count += 1
                
    
LL = LinkedList()
n = int(input())
LL.length()
for i in range(n):
    data = int(input())
    LL.insert_at_ending(data)
    
data2 = int(input())
LL.insert_at_beginning(data2)

data3 = int(input())
index = int(input())
LL.insert_at_middle(data3,index)
index1 = int(input())
LL.remove(index1)
LL.display()
