def minimum_distances(a):
    d = {}
    n = len(a)
    min_diff = n
    for i in range(n):
        try:
            min_diff = min(i-d[a[i]], min_diff)
            d[a[i]] = i
            if min_diff == 1:
                break
        except:
            d[a[i]] = i
    return -1 if min_diff == n else min_diff


print(minimum_distances([7, 1, 3, 4, 1, 7]) == 3)
print(minimum_distances([1, 2, 3, 4, 10]) == -1)
