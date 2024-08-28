def partition_array(array):
    if len(array) == 0:
        return array 

    pivot = array[-1]
    j = 0
    
    for i in range(len(array) - 1):
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]
            j += 1
    
    array[j], array[-1] = array[-1], array[j]
    
    return array
