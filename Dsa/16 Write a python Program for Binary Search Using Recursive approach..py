def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid


    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)


    else:
        return binary_search(arr, target, mid + 1, high)


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = 40

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
