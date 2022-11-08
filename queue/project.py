# let's create  a project over stack ; 
class Stack: 
    def  __init__(self):
        self.lst=[]
    def push(self,data):
        if data == 0 :
            self.lst.insert(0,data)
        else:
            self.lst.append(data)
    def pop(self):
        return self.lst.pop()
    def peak(self) : 
        return self.lst[-1]
    def size(self):
        return  len(self.lst)
    
    
c= Stack()

c.push(0)

c.push(1)
c.push(1)
c.push(1)
c.push(1)
c.push(1)

c.push(0)

c.push(1)

c.push(1)
c.size()
print(c.lst)
print(c)
