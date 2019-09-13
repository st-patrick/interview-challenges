# using a "worm" approach: move to next character and append to a 
# "candidate" list until there are three different characters in 
# the candidate. Then, save the length.

def findSequence(seq):
  sequence_candidate = []
  longest_seq = 0

  for char in seq:
    sequence_candidate.append(char)
    char_amount = len(set(sequence_candidate))
    curr_len = len(sequence_candidate)
    if char_amount > 2:
	longest_seq = curr_len - 1
	print "current longest sequence is " + str(sequence_candidate[:-1])
	while (char_amount > 2):
		sequence_candidate.pop(0)
		char_amount = len(set(sequence_candidate))
    elif len(sequence_candidate) > longest_seq:
	longest_seq = curr_len


  print "found longest sequence: " + str(sequence_candidate)
  return longest_seq

  



print findSequence([1, 3, 5, 3, 1, 3, 1, 5])
# 4
print findSequence([1, 3, 6, 9, 7, 3, 1, 4, 3, 4, 5, 5, 5, 5, 5])
# 6
print findSequence([4, 3, 5, 6, 7, 1, 1, 2, 3, 8, 9, 2, 4, 3, 9, 4, 5, 6, 5, 6])
# 4
