def bubbleSort(array):

    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

array = [8, 2, 6, 4, 5]
sorted_array = bubbleSort(array)
print(sorted_array)

# Time Complexity: O(n²) (like comparing every bubble with every other bubble).
# Space Complexity: O(1) (no extra space needed!).