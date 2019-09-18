# TODO create explicit function calculating the possibilities
# by using the binomial coefficient
# you can either see this is true by filling out a grid of
# solutions and how they add up or you can imagine
# the grid being a series of m-1 choices to go right (= 1)
# and n-1 choices to go down (= 0). Then, all we need is a 
# formula for how to calculate the permutations of m-1 1s and
# n-1 0s

# again with the self-similarity.
# obviously this applies: num_ways(m,n) = num_ways(m-1,n) + num_ways(m,n-1)
# also, with some logic we know that a single column or row of length x
# has only 1 way to be traversed (all the way right or down)
# combined we get:

def num_ways(n, m):
	if n == 1:
		return 1
	if m == 1:
		return 1

	return num_ways(n-1,m) + num_ways(n,m-1)
		


print num_ways(2, 2)
# 2
print num_ways(3,2)
# 3
print num_ways(3,3)
# 6
print num_ways(4,3)
# 10
print num_ways(6,8)
print num_ways(8,6)
# 792
print num_ways(4,4)
# 20
