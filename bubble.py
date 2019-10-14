
def bubbleSort(arr):
    n = len(arr)
    tat = 0
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                tat+= 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return tat
# Driver code to test above
arr = [8, 22, 7, 9, 31, 5, 13]

k = bubbleSort(arr)
print(k)
