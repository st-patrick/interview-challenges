# we have a staircase of n steps
# each climb is either 1 or 2 steps. How many ways to climb stairs, given
# staircase of n steps are there?

# this problem greatly displays self-similarity. At each point on the
# staircase we have two options: take 1 step or take 2 steps. Of course, after
# that, we have the problem of how many possibilities there are for n-1 and
# n-2 steps.
# Starting at a staircase with 1 step, we can easily work up to that and
# fill a list with all the possibilities of a staircase with n steps
# usind this formula: staircase(n) = staircase(n-1) + staircase(n-2)
# We can easily, manually see that staircase(1) = 1 and staircase(2) = 2.
# after that, it's just addition like the Fibonacci sequence

memory = [1,2]

def staircase(n):
  if n > len(memory):
    for i in range(len(memory), n):
      memory.append(memory[i-1] + memory[i-2])

  return memory[n-1]  


  
print staircase(4)
# 5
print staircase(5)
# 8
