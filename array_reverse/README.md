# Reverse an Array
- The function has a paramater and this paramter should be an array.
- for example we have this array : [0,1,2,3], we have to push the first element to the last index which give us this result Output : [3,2,1,0].


## Whiteboard Process
![WhiteBoard image](/array-reverse1.jpg)

## Approach & Efficiency
- What approach did you take?
    - Swap the first half array with second one.

- Discuss Why.
    swap element in the same array will create a reverse array without the need to create a new array.

- What is the Big O space/time for this approach?
    - I understand the Big O but I didn't fully understand it yet.

## Another way to reverse an array (python)
def reverseArray(Array):
    newArr = Array[::-1]
    return print(newArr)

reverseArray([10,22,15,0])
