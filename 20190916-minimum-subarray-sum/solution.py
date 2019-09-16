# we are going to use the same 'rainworm' approach as in the last challenge
# going through the array, we add numbers to a sum. If the sum is smaller than
# s, we keep adding numbers. If it's larger, we start removing numbers from
# the beginning. If the sum equals s, we have found a solution and remember
# the length of the subarray.

class Solution:
  def minSubArrayLen(self, nums, s):
    pointer_left = 0
    pointer_right = 0
    sum = 0
    min_subarray = 0

    for num in nums:
	if sum <= s:
		sum += num
		
	
	print "now checking " + str(pointer_left) + " to " + str(pointer_right) + " : " + str(nums[pointer_left:pointer_right+1]) + " (sum: " + str(sum) + ")"
		
	while(sum > s):
		sum -= nums[pointer_left]
		pointer_left += 1
		print "array too big. reduced: " + str(nums[pointer_left:pointer_right+1])  + " (sum: " + str(sum) + ")"


        if sum == s:
		print "found fit " + str(nums[pointer_left:pointer_right+1])  + " (sum: " + str(sum) + ")"
		length = (pointer_right - pointer_left) + 1
		if length < min_subarray or min_subarray == 0:
	                min_subarray = length

	pointer_right += 1

    return min_subarray


print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)
# 2
print Solution().minSubArrayLen([2, 3, 1, 2, 99, 3], 99)
# 1
print Solution().minSubArrayLen([2, 3, 8, 2, 3, 3], 13)
# 3
