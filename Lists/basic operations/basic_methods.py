# LINKED LISTS
# NOTE: How is Linked list better than arrays?
# NOTE: Benefits of Linked List?

# TITLE: NODE STRUCTURE
class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next


# TITLE: LINKEDLIST STRUCTURE
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("Linked list is Empty")
            return 
        curr=self.head
        lstr=''
        while(curr):
            lstr=lstr+str(curr.data)+'-->'
            curr=curr.next
        
        lstr=lstr+'X'
        print(lstr)
    
    def insertAtEnd(self,data):
        node=Node(data,None)
        if(self.head is None):
            self.head=node
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=node
            
    def insert_values(self,data_list):
        self.head=None
        for x in data_list:
            self.insertAtEnd(x)
    
    def getLength(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        print("Length is: ",count)
        return count
    
    def removeAt(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        curr=self.head
        while(curr):
            if count==(index-1):
                print("deleting ",curr.next.data)
                curr.next=curr.next.next
                break
            count+=1
            curr=curr.next
            
    def insertAt(self,index, data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        node=Node(data,None)
        if index==0:
            node.next=self.head
            self.head=node
            return 
        curr=self.head
        count=0
        while(curr):
            if count==index-1:
                node.next=curr.next
                curr.next=node
                break
            curr=curr.next
            count+=1   
            
# OPERATIONS
ll=LinkedList()
ll.insert_at_beginning(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.print()
ll.removeAt(0)
ll.removeAt(3)
ll.print()
ll.insertAt(2,"hi")
ll.print()
print("--------------------")
ll.insert_values(["apple", "banana", "carrot","orange"])
ll.print()
ll.getLength()