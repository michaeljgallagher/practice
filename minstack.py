'''
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((x, min(curr_min, x)))
    
    def pop(self):
        return self.stack.pop()[0]
        
    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
        
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
