class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    
    def __init__(self):
        self.head=None
    
    def insertbegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    
    def insertend(self,data):
         new_node=Node(data)
         if self.head is None:
            self.head=new_node
         else:
             current_node=self.head
             while current_node.next:
                 current_node=current_node.next
             current_node.next=new_node
    
    def deletebegin(self):
        if self.head is None:
            print("Linklist is empty")
        else:
            self.head=self.head.next
    
    def deleteend(self):
        if self.head is None:
            print("Linklist is empty") 
        else:
            current_node=self.head
            prev=None
            while current_node.next:
                prev=current_node
                current_node=current_node.next
                prev.next=None                              
                
    def size(self):
        if self.head is None:
            print("Linklist is empty")
        else:
            current_node=self.head
            count=0
            while current_node:
                current_node=current_node.next
                count+=1                
            print("\nSize of linklist is", count)
    def printll(self):
        current_node=self.head
        while current_node:
            print(current_node.data) 
            current_node=current_node.next
    
    
l1=linklist()
while True:
    print("\nLink list operations")
    print("1.insert at begin")
    print("2.insert at end")
    print("3.Delete at begin")
    print("4.Delete at end")
    print("5.Size")
    print("6.display")
    print("7.Exit")
    c=int(input("Enter choice:"))
    
    if c==1:
        e=int(input("Enter data:"))
        l1.insertbegin(e)
    
    elif c==2:
        e=int(input("Enter data:"))
        l1.insertend(e)
    
    elif c==3:
        l1.deletebegin()
    
    elif c==4:
        l1.deleteend()
    
    elif c==5:
        l1.size()
    
    elif c==6:
        l1.printll()
    
    elif c==7:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice")                    