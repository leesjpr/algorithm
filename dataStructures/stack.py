class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return self.items == []


    def push(self, item):
        self.items.append(item)
        #self.items.insert(0, item)


    def pop(self):
        return self.items.pop()
        #return self.items.pop(0)


    def peek(self):
        return self.items[len(self.items)-1]
        #return self.items[0]


    def size(self):
        return len(self.items)



s = Stack()

print s.is_empty()
s.push(4)
s.push('dog')
print s.peek()
s.push(True)
print s.size()
print s.is_empty()
