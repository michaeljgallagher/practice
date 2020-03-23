'''
You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height. You can change the height of a stack by removing
and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are
exactly the same height. This means you must remove zero or more cylinders from
the top of zero or more of the three stacks until they're all the same height,
then print the height. The removals must be performed in such a way as to
maximize the height. 
'''

def equal_stacks(h1, h2, h3):
    stacks = [h1, h2, h3]

    for stack in stacks:
        stack.reverse()
        for i in range(1,len(stack)):
            stack[i] = stack[i] + stack[i-1]
        stack.reverse()
    stacks.sort(key=len)

    for x in stacks[0]:
        flag = True
        for stack in stacks[1:]:
            if x not in stack:
                flag = False
                break
        if flag:
            return x
        
    return 0


