def selectionSort(array):

    for i in range(0, len(array) - 1):
        min = i

        for j in range( i + 1, len(array) ):
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array

array = [8, 2, 6, 4, 5]
sorted_array = selectionSort(array)
print(sorted_array)

# Time Complexity: O(n²) (not the fastest, but easy to understand!).
# Space Complexity: O(1) (no extra space needed!).