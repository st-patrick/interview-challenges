# Here's the idea: for every letter at position x in the shorter or equal string "needles", we find
# the same letter in the other string "haystack" with minimal distance.
# The position of that letter in the "haystack" will be f(x).
# This defines f(X), given that X is range 0...len(needles)

# current approach: We find out, how many "crossings" of "lines" we have,
# mathematically speaking, we determine whether a < b && f(a)>=f(b).
# then, we create a list of all such encounters and "take out" the indices
# which have the most crossings each until we do not have any crossings
# anymore. Based on the remaining minimal distances, we can now calculate, 
# how many letters need to be replaced / inserted / deleted


def distance(s1, s2):
  # pick the shorter word and try to "stretch" it
  needles = (s1 if s1 < s2 else s2)
  haystack = (s2 if s1 < s2 else s1)
  print(needles)

  distance_array = []
  fillDistanceArray(distance_array, needles, haystack)
  print distance_array
  
#  for needle in needles:





# this will fill a list of minimal distance to the same letter from a needle
# in a word to a that needle in the haystack
def fillDistanceArray(distance_array, needles, haystack):
  counter = 0
  for needle in needles:
    distance_array.append(getShortestLetterDistance(needle, counter, haystack)) 
    counter += 1


# determines the minimal distance of a given letter at given index to 
# the same letter in the haystack. if needle is not found, returns None
def getShortestLetterDistance(needle, index, haystack):
  # default to not found
  delta = None

  print "starting with word " + haystack
  
  counter = 0
  found = False
  reached_left = False
  reached_right = False
  while not found:
    if index-counter >= 0: # prevent index out of bounds error
      left = haystack[index-counter]
    else:
      reached_left = True
    if index+counter < len(haystack):
      right = haystack[index+counter]
    else:
      reached_right = True

#    print left
#    print right

    if left == needle or right == needle:
      found = True
    elif not reached_left or not reached_right:
      counter += 1
    else:
      break

  if found:
    delta = counter


  return delta


         
print distance('biting', 'sitting')
# 2


print "shortest distance for letters tests:"
print getShortestLetterDistance('c', 2, "abbrhgcweihwg")
#4
print getShortestLetterDistance('z', 8, "zabbrhgcweihwg")
#8
