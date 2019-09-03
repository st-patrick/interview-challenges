def two_sum(list, k):
  subtracted = set()
  # we create a set containing all possible k - num
  # since we are looking for a num in list that fulfills
  # num + x = k we can store all possible k - num
  # then, if another num2 = k - num we know that num + num2 = k
  for num in list:
    if num in subtracted: return True
    subtracted.add(k - num)

  return False

print two_sum([4,7,1,-3,2], 5)
# True

print two_sum([5,1,2,3], 6)
