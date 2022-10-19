from array import *
class ArrayQ():
    def __init__(self, ko = []):
        self._array = ko
    def enqueue(self, x):
        self._array.append(x)
    def dequeue(self):
        return self._array.pop(0)
    def Queue(self):
        self._array = []
    def isEmpty(self):
        if len(self._array) == 0:
            return True
        else:
            return False
    def size(self):
        return(len(self._array))

"""q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")"""
