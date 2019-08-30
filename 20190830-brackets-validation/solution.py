class Solution:
  curly_balance = 0
  parentheses_balance = 0
  square_balance = 0

  def isValid(self, s, debug = False):
    curly_balance = 0
    parentheses_balance = 0
    square_balance = 0
    pointer = 0
    closed = False

    while (pointer < len(s)):
      b = s[pointer]
      if debug: print "pointer"
      if debug:  print pointer
      closed = False

      if b == '{': curly_balance += 1
      elif b == '}':
	if s[pointer-1] != '{': return False
	curly_balance -= 1
	closed = True
      elif b == '(': parentheses_balance += 1
      elif b == ')':
	if s[pointer-1] != '(': return False
	parentheses_balance -= 1
	closed = True
      elif b == '[': square_balance += 1
      elif b == ']':
	square_balance -= 1
	if s[pointer-1] != '[': return False
	closed = True

      # create a new string without the closed brackets "Tetris Style" so our string is a stack of opened brackets
      if closed:
	if debug: print "eliminating" + s
	if debug: print "           " + ' '*(pointer) + '^'
	left = pointer-1
	s = s[:left] + s[pointer+1:]
	pointer -= 1
      else:
        pointer += 1

      if debug: print "curly "
      if debug: print curly_balance
      if debug: print "parentheses "
      if debug: print parentheses_balance
      if debug: print "square "
      if debug: print square_balance
      if debug: print s
      if debug: print ' '*(pointer) + '^'

    return (curly_balance == 0 and parentheses_balance == 0 and square_balance == 0)


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "((()))"
# should return True
print(Solution().isValid(s))

s = "[()]{}"
# should return True
print(Solution().isValid(s))

s = "({[)]"
# should return False
print(Solution().isValid(s))
