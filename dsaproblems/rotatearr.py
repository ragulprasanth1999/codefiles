def rotateArray(arr, k):
    for i in range(k):
        v = arr[0]  
        arr.pop(0)  
        arr.append(v)  
    return arr