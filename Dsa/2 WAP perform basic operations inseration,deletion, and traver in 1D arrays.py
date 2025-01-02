from array import array

# create the array
arr = array('i',[1,2,3,4,5,6,7,8])
print(arr)

#Traversal
for i in arr:
    print(i,end=' ')

# deletion
arr.remove(3)
# Insertion
arr[4]= 100
print(arr)