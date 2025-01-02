def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid


        elif arr[mid] > target:
            high = mid - 1


        else:
            low = mid + 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 40

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
