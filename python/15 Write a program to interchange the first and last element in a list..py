def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


input_list = [10, 20, 30, 40, 50]
print("Original list:", input_list)

result = interchange_first_last(input_list)
print("List after swapping first and last elements:", result)
