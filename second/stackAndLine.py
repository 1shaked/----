from __future__ import annotations

class Stack:
    def __init__(self, els: list[int]):
        self.els: list[int] = els

    def pop(self) -> int:
        return self.els.pop()
    
    def push(self, el) -> None:
        self.els.append( el)

    def isEmpty(self) -> bool:
        return len(self.els) == 0

    def isNotEmpty(self) -> bool:
        return not self.isEmpty()


class Line:
    def __init__(self):
        self.s1: Stack = Stack([])
        self.s2: Stack = Stack([])
    
    def push(self, el) -> None:
        self.switchBetweenStacks()
        if self.s1.isNotEmpty():
            self.s1.push(el)
        else:
            self.s2.push(el)
        self.switchBetweenStacks()        


    def switchBetweenStacks(self) -> None:
        if self.s1.isNotEmpty():
            for _ in range(len(self.s1.els)):
                el = self.s1.pop()
                self.s2.push(el)
            return 
        elif self.s2.isNotEmpty:
            for _ in range(len(self.s2.els)):
                el = self.s2.pop()
                self.s1.push(el)
        

    def pop(self) -> int:
        if self.s1.isNotEmpty:
            return self.s1.pop()
        return self.s2.pop()



# show you how to implement a line with two stack

L: Line = Line()

for i in range(5):
    L.push(i)


for i in range(5):
    print(L.pop())

