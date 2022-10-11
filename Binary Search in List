def binary_search(sorted_lst, left_index, right_index, x):
  while left_index <= right_index:
    mid_index = left_index + (right_index - left_index) // 2
    if sorted_lst[mid_index] == x:
      return mid_index
    elif sorted_lst[mid_index] < x:
      left_index = mid_index + 1
    else:
      right_index = mid_index - 1
  return -1


lst = [0, 5, 2, 3, 4, 1, 6, 7, 8, 9, 10]
x = 1
print(binary_search(lst, 0, len(lst) - 1, x))

#output: 5
