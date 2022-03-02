import math
def insert_shift_array(Arr,newVal):
    n = math.ceil(len(Arr)/2)
    i = len(Arr)
    Arr += [0]
    while (i >= n):
        if (i == n):
            Arr[i] = newVal
        else: 
            Arr[i] = Arr[i-1]
        i-=1
    return Arr
print(insert_shift_array([0,1,2,3,4],"x"))

def deleteElementArr(Arr):
    Middle = math.floor(len(Arr)/2)
    n = len(Arr)
    return [Arr[i] for i in range(n) if i != Middle]
print(deleteElementArr([0,1,2,3,4]))