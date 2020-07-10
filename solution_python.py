class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
class EventSourcer():
    # Do not change the signature of any functions    
    
    def __init__(self):
        self.value = 0
        self.state = 0

    def add(self, num: int):        
        self.value += num
        s.push(self.value)
        return self.value

    def subtract(self, num: int):
        self.value -= num
        s.push(self.value)
        return self.value

    def undo(self):
        if s.isEmpty():
            return "Nothing to Undo"
        self.state = s.peek()
        self.value = self.state
        s.pop()
        return s.peek()

    def redo(self):  
        if self.state != 0:
            s.push(self.state)
            self.value = self.state
        else:
            return "Nothing to redo"
        return s.peek()

    def bulk_undo(self, steps: int):
        if s.isEmpty() :
            return "Noting to Undo"
        else:
            for i in range(steps):
                self.undo()

    def bulk_redo(self, steps: int):
        if s.isEmpty() :
            return "Noting to Redo"
        else:
            for i in range(steps):
                self.redo()