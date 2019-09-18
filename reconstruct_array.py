def reconstruct(arr):
    '''
    The sequence [0, 1, ..., N] has been jumbled, and the only clue
    you have for its order is an array representing whether each number
    is larger or smaller than the last. Given this information,
    reconstruct an array that is consistent with it. For example, given
    [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
    '''
    N = len(arr) - 1
    stack = []
    ans = []

    for i in range(N):
        if arr[i+1] == '-':
            stack.append(i)
        else:
            ans.append(i)
            while stack:
                ans.append(stack.pop())

    stack.append(N) #need to append last element seperately

    while stack:
        ans.append(stack.pop())

    return ans

print(reconstruct([None, '+', '+', '-', '+']))
print(reconstruct([None, '+', '+', '+', '+']))
print(reconstruct([None, '-', '-', '-', '-']))
print(reconstruct([None, '-', '+', '-', '+']))
print(reconstruct([None, '+', '-', '+', '-']))
print(reconstruct([None, '+', '-', '-', '+']))
print(reconstruct([None, '-', '+', '+', '-']))
