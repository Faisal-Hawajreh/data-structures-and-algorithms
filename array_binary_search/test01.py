import math

Arr = [0,1,2,3,4,5]

def binary_search(Arr,key):
    i = 0
    j = len(Arr)-1
    n = math.floor(len(Arr)/2)
    idx = math.floor(len(Arr)/2)
    if key not in Arr: return -1
    while i<=j:
        print(Arr,idx,n,j)
        if Arr[n] == key:
            return idx
        else:
            if Arr[i] <= key < Arr[n]:
                Arr = Arr[:n]
                n = math.floor(len(Arr)/2)
                idx -= (len(Arr) - n)
            else:
                Arr = Arr[n+1:]
                n = math.floor(len(Arr)/2)
                idx += n+1

        j = len(Arr) -1

print(binary_search(Arr,2))
