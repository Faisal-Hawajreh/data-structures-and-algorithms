def reverseArray(Array):
    newArr = []
    n = len(Array)
    for i, element in enumerate(Array):
        newArr.insert(i,Array[n-1-i])
    return print(newArr)
reverseArray([10,22,15,0])

# def reverseArray(Array):
#     newArr = Array[::-1]
#     return print(newArr)

# reverseArray([10,22,15,0])