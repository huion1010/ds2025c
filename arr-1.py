import array
def move(arr):
    zero = 0
    for index, n in enumerate(arr):
        if n != 0:
            arr[zero] = n
            if zero != index:
                arr[index] = 0
            zero += 1
    return(arr)

arr = array.array('i', [99, 0, -7, 0, 16])
move(arr)
print(arr)
