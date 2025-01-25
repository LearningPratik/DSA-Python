def quickSort(array):

    # base case
    if (len(array) <= 1):
        return array
    
    pivot = array[-1]
    left = []
    right = []

    for num in array[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quickSort(left) + [pivot] + quickSort(right)

import numpy as np
import random
array1 = np.random.randint(low = 0, high = 100, size = (50, 1))

array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print("Sorted array:", quickSort(array))
