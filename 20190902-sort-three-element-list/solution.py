def sortNums(nums):
  smallest_counter = 0
  mid_counter = 0
  largest_counter = 0
  for num in nums:
    if num == 1: smallest_counter += 1
    elif num == 2: mid_counter += 1
    elif num == 3: largest_counter += 1

  return ([1] * smallest_counter + [2] * mid_counter + [3] * largest_counter)

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
