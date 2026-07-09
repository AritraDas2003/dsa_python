def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Main Program
arr = []

n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

selection_sort(arr)

print("Sorted array:")
for i in arr:
    print(i, end=" ")