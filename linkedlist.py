class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        node1=Node(90)
        print(node1)

class LinkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end="")
                n=n.ref
                print("Null")

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                n.ref=new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print ("Node is not present in Linked List")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty so we can't delete any node")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty so we can't delete any node")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
                n.ref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("Can't perform delete operation in empty linked list")
        else:
            if x == self.head.data:
                self.head=self.head.ref
            else:
                n=self.head
                while n.ref is not None:
                    if x == n.ref.data:
                        break
                    n=n.ref
                if n.ref is None:
                    print("Node to be deleted is not present")
                else:
                    n.ref=n.ref.ref

LL=LinkedList()
LL.add_begin(80)
LL.add_begin(90)
LL.add_begin(40)
LL.add_begin(70)
LL.add_begin(35)
LL.add_end(40)
LL.add_after(80,90)
LL.delete_begin()
LL.delete_end()
LL.delete_by_value(90)
LL.print_LL()
