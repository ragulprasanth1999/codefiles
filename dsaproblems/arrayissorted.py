def isSorted(n,a):
    n = len(a)
    for i in range(1, n):
        if a[i] <a[i - 1]:
            return 0
    return 1