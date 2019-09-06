class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  pointer = root_node

  while (pointer.value is not None):
    if k < pointer.value:
      ceil = pointer.value
      if pointer.left is not None:
        pointer = pointer.left
      else: break

    elif k > pointer.value:
      floor = pointer.value
      if pointer.right is not None:
	pointer = pointer.right
      else: break

    elif k == pointer.value: return [k, k]

  return [floor, ceil]


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)

print findCeilingFloor(root, 11)
# (10, 12)


root = Node(32)
root.left = Node(16)
root.right = Node(48)

root.left.left = Node(8)
root.left.right = Node(24)

root.right.left = Node(40)
root.right.right = Node(56)

root.left.left.left = Node(4)
root.left.left.right = Node(12)

root.left.right.left = Node(20)
root.left.right.right = Node(28)

root.right.left.left = Node(36)
root.right.left.right = Node(44)

root.right.right.left = Node(52)
root.right.right.right = Node(60)


print findCeilingFloor(root, 5)
# (4, 8)

print findCeilingFloor(root, 21)
# (20, 24)
