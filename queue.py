class queuesArray:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0

    def enqueue(self,e):
        self.data.append(e)

    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self.data.pop(0)

    def first(self):
        if self.isempty():
            print("Queue is Emoty")
            return
        return self.data[0]

q=queuesArray()
q.enqueue(92)
q.enqueue(99)

print(q.data)
print("Length:",len(q))

q.enqueue(7)
q.enqueue(11)

print(q.data)
print(q.dequeue())
print(q.data)
print(q.first())
