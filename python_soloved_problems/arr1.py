def getSecondOrderElements(n: int, a):
    var1 = min(a)
    var2 = max(a)
    a.remove(var1)
    a.remove(var2)
    smin = min(a)
    smax = max(a)
    return [smin, smax]

# Example usage:
n = 5
a = [1, 3, 2, 5, 4]
result = getSecondOrderElements(n, a)
print(result)  # Output: [2, 4]
