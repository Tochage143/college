
def linear_search(arr, target):

    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


arr = [34, 78, 12, 89, 56, 23, 45]


target = 89


result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
