def check(lst):
  pointer = 0
  decreasing_counter = 0
  while pointer < len(lst)-1:
	if lst[pointer] > lst[pointer+1]: decreasing_counter += 1
	pointer += 1
  return decreasing_counter < 2

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False
print check([3,4,5,8,9,1,2,3,4,2])
# False
