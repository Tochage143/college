from array import array

# create the array with array module
arr = array('i',[1,2,3,4,5,6])
print(arr)

print(f'the first element of array {arr[0]}')

#Change the position of 1 index
arr[1]= 22
print(arr)

#Add at the end
arr.append(7)
print(arr)

#Remove the element 22
arr.remove(22)
print(arr)