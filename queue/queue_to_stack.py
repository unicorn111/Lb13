import copy
from arraystack import *
from linkedqueue import *


class QueueStack:
    def __init__(self, queue):
        self.queue = queue

    def isEmpty(self):
        return self.queue.isEmpty()

    def __len__(self):
        return self.queue.__len__()

    def pop(self):
        st2 = copy.deepcopy(self.queue)
        st1 = ArrayStack()
        st3 = ArrayStack()
        for i in range(len(st2)):
            j = st2.peek()
            st2.pop()
            st1.push(j)
        st1.pop()
        for i in range(len(st1)):
            j = st1.peek()
            st1.pop()
            st3.push(j)
        for i in range(len(st3)):
            j = st3.peek()
            st3.pop()
            st2.add(j)
        self.queue = st2
        return self.queue

    def peek(self):
        st2 = copy.deepcopy(self.queue)
        st1 = ArrayStack()
        for i in range(len(st2)):
            j = st2.peek()
            st1.push(j)
            st2.pop()
        n_p = st1.peek()
        return n_p

    def push(self, item):
        self.queue.add(item)
        return self.queue


def check():
    b = LinkedQueue()
    b.add('lol')
    b.add('ball')
    b.add('foo')
    b.add('boo')
    a = QueueStack(b)
    print(a.isEmpty())
    print(a.peek())
    print(a.pop())
    print(a.push('lili'))
check()
