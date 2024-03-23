def getSecondOrderElements( a):
    var1 = min(a)
    var2 = max(a)
    a = [x for x in a if x != var1 and x != var2]  # Remove all instances of min and max
    smin = min(a)
    smax = max(a)
    return [smax, smin]