from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
        self.q.rotate(1)   
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return not self.q
        