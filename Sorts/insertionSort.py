def insertionSort(array):

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while ( j >=0 and temp < array[j] ):
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = temp

    return array

array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_array = insertionSort(array)
print(sorted_array)