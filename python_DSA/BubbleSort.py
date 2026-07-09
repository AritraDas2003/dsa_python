def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Main Program
arr = []

n = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

bubble_sort(arr)

print("Sorted array:")
for i in arr:
    print(i, end=" ")