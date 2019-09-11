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
  needles = (s1 if len(s1) < len(s2) else s2)
  haystack = (s2 if len(s1) < len(s2) else s1)
  print("needles is " + needles)
  print("haystack is " + haystack)

  distance_array = []
  fillDistanceArray(distance_array, needles, haystack)
  print distance_array

  image_lookup = []
  determineFunction(image_lookup, needles, haystack)
  print image_lookup

  # initialize the "amount of crossings" lookup triangular table
  crossings_lookup = [[None for y in xrange(len(image_lookup))] for x in xrange(len(image_lookup))]
  crossings_counts = [ 0 for x in xrange(len(image_lookup))]
  crossings_links = [[] for x in xrange(len(image_lookup))]
  countCrossings(crossings_lookup, crossings_counts, crossings_links, image_lookup)
  print crossings_lookup
  print crossings_counts
  print crossings_links

#  for needle in needles:



# ok, here's to some horrible code. We now want to eliminate all crossings starting with the lines
# with the most crossings
def eliminateCrossings(crossings_counts, crossings_links):
  maximum = 0
  index_max = None
  while True:
    for index in xrange(len(crossings_counts)):
      if crossings_counts[index] > maximum:
	maximum = crossings_counts[index]
	index_max = index
    if maximum == 0: break
    else: eliminateLine(index, crossings_counts, crossings_links)


# TODO write this
def eliminateLine(index, crossings_counts, crossings_links):
  return;


# now, we simply run the abovementioned logical comparison and will end up with a list of lists
# of Boolean values (cross or don't cross, True or False)
def countCrossings(crossings_lookup, crossings_counts, crossings_links, image_lookup):
  for a_index in xrange(len(image_lookup)):
    for b_index in xrange(a_index+1, len(image_lookup)):
      if image_lookup[a_index] is None or image_lookup[b_index] is None:
	crossings_lookup[a_index][b_index] = False
      elif image_lookup[a_index] >= image_lookup[b_index]:
        crossings_lookup[a_index][b_index] = True
	crossings_links[a_index].append(b_index)
        crossings_links[b_index].append(a_index)
	crossings_counts[a_index] += 1
	crossings_counts[b_index] += 1
      else:
	crossings_lookup[a_index][b_index] = False
    


# basically the same mechanic, hence we can use the other functions and have them
# return where they found the closes neighbor instead of the distance
def determineFunction(image_lookup, needles, haystack):
  return fillDistanceArray(image_lookup, needles, haystack, True)


# this will fill a list of minimal distance to the same letter from a needle
# in a word to a that needle in the haystack
def fillDistanceArray(distance_array, needles, haystack, return_indices = False):
  counter = 0
  for needle in needles:
    print "determine distance for " + needle
    distance_array.append(getShortestLetterDistance(needle, counter, haystack, return_indices)) 
    counter += 1


# determines the minimal distance of a given letter at given index to 
# the same letter in the haystack. if needle is not found, returns None
def getShortestLetterDistance(needle, index, haystack, return_index = False):
  # default to not found
  delta = None
  found_at = None

  print "starting with word " + haystack
  
  counter = 0
  found = False
  reached_left = False
  reached_right = False
  while not found:
    print counter
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

    if left == needle:
      found = True
      found_at = index - counter
    elif right == needle:
      found = True
      found_at = index + counter  
    elif not reached_left or not reached_right:
      counter += 1
    else:
      break

  if found:
      delta = counter
      
  return found_at if return_index else delta


         
print distance('biting', 'sitting')
# 2
print distance('superfreak', 'superfanatical')
# ???


print "shortest distance for letters tests:"
print getShortestLetterDistance('c', 2, "abbrhgcweihwg")
#4
print getShortestLetterDistance('z', 8, "zabbrhgcweihwg")
#8
