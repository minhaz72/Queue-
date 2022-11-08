# Let's create a enqueu and deque : 
from re import L


class Queue:
    def __init__(self): 
        self.lst=[]
    def isEmpty(self):
        return self.lst==[]
    def append(self,data) :
        self.lst.append(data)
    def prepend(self,data) : 
        self.lst.insert(0,  data)
    def  pop (self): 
        return self.lst.pop()
    def peak(self):
        return self.lst[-1]
    def size(self): 
        return len(self.lst)

q= Queue()
q.isEmpty()
q.append('ap')
q.append('o')
q.prepend('hi')
print(q.lst)

    