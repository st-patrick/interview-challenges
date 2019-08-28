class Solution:
  def lengthOfLongestSubstring(self, s):
    length = 0
    longest = 0
    prev = None
    
    for char in s:
      curr = char
      length = length + 1
      if curr is prev:
        if length > longest: longest = length
        length = 0
      prev = curr

    if length > longest: longest = length # in case there is no repetition in the end

    return longest

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
print Solution().lengthOfLongestSubstring('dddhjkegkergaukgfbbbasdfmbalkgvlertv.awirghasddddddsfgr')
# 27
print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxxasdfasdfasdfasdf')
