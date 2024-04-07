def getSecondOrderElements(n: int, a):
    var1 = min(a)
    var2 = max(a)
    a = [x for x in a if x != var1 and x != var2]  # Remove all instances of min and max
    smin = min(a)
    smax = max(a)
    return [smax, smin]

# Example usage:
n = 5
a = [1, 3, 2, 5, 4]
result = getSecondOrderElements(n, a)
print(result)  # Output: [2, 4]
