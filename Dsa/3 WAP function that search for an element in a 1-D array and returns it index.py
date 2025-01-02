from array import array

arr = array(
    'i',
    [1,2,3,4,5,6,7,8,9,10]
)

def search(arr,search_item ):
    for i in range(len(arr)):
        if i == search_item:
            return i


print(f'itme find at position {search(arr,2)}')