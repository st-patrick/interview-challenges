class Solution:
  def lengthOfLongestSubstring(self, s):
    solution = ""
    prev = None
    for char in s:
      curr = char
      if curr is prev:
        break
      solution += curr
      prev = curr
    return solution

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
