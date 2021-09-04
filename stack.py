class stacksArray:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0

    def push(self,e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return
        return self.data.pop()

    def top(self):
        if self.isempty():
            print("Stack is Emoty")
            return
        return self.data[-1]

s=stacksArray()
s.push(int(input("Enter the number to be inserted:")))
s.push(int(input("Enter the number to be inserted:")))

print(s.data)
print("Length:",len(s))
print(s.pop())
print(s.isempty())
print(s.pop)

s.push(int(input("Enter the number to be inserted:")))
s.push(int(input("Enter the number to be inserted:")))

print(s.data)
print(s.top())
print(s.data)
