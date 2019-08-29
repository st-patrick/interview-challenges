#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"
class Solution: 
    champion = ""

    def longestPalindrome(self, s):
      longest = 1 #because every character is a palindrome in itself
      left = ''
      self.champion = ""
      pointer = 0
      for c in s:
        # optimization: abort loop if longest palindrome is alrady longer than any new one could be
	length = 1        
	contestant = str(c)
	found_start = False

	if (pointer + 1 < len(s) and c == s[pointer + 1]):  # palindrome with even amount of characters
	  contestant += str(s[pointer+1])
	  left = pointer - 1 # initialize pointer to go over the char left and right to check symmetry
	  right = pointer + 2
	  found_start = True
	elif (pointer > 0):  # palindrome with uneven amount of characters
	  left = pointer - 1
	  right = pointer + 1
	  found_start = True

	if found_start:
	  while (left > -1 and right < len(s) and s[left] == s[right]):
	    length = length + 2
	    contestant = s[left] + contestant + s[right]
	    left = left - 1
	    right = right + 1

	# have we found a new champion?
	if length > longest:
	  longest = length
	  self.champion = contestant
        
	pointer = pointer + 1 #move our pointer. Guess I could just use a for loop

      return self.champion

def test(s):
  print(str(Solution().longestPalindrome(s)))
        
# Test program
test("tracecars")
# racecar

test("ratatat")
# atata, since it will pick the first possibility

test("banana")
#Output: "anana"

test("million")
#Output: "illi"
