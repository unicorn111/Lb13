import copy
from arraystack import *


class StackQueue:
    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        return self.stack.isEmpty()

    def __len__(self):
        return self.stack.__len__()

    def clear(self):
        for i in range(len(self.stack)):
            self.stack.pop()
        return self.stack

    def peek(self):
        st2 = copy.deepcopy(self.stack)
        st1 = ArrayStack()
        for i in range(len(st2)):
            j = st2.peek()
            st2.pop()
            st1.push(j)
        n_p = st1.peek()
        return n_p

    def pop(self):
        st2 = copy.deepcopy(self.stack)
        st1 = ArrayStack()
        for i in range(len(st2)):
            j = st2.peek()
            st2.pop()
            st1.push(j)
        st1.pop()
        for i in range(len(st1)):
            j = st1.peek()
            st1.pop()
            st2.push(j)
        self.stack = st2
        return self.stack

    def add(self, item):
        self.stack.push(item)
        return self.stack





def check():
    b = ArrayStack()
    b.push('lol')
    b.push('ball')
    a = StackQueue(b)
    print(a.isEmpty())
    print(a.peek())
    print(a.pop())
    print(a.peek())
    print(len(a))
    print(a.add('pupi'))
    print(len(a))
    print(a.isEmpty())
check()