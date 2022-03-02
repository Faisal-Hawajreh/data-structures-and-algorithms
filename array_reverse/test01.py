from array import array
import math
def reverse_array(Arr):
    n = len(Arr)-1
    i = 0
    while (i <= math.floor(n/2)):
        Arr[i],Arr[n-i] = Arr[n-i],Arr[i]
        i+=1
    return Arr
reverse_array([10,22,1,15,0])

# def reverse_array(Array):
#     newArr = Array[::-1]
#     return print(newArr)

# reverse_array([10,22,15,0])