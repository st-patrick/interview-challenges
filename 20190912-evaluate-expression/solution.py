# We will start with a simple solution that passes the test
# But relies on the expression only having bracktes around
# the right part of an expression

def eval(expression):
  digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  operators = ['-', '+']
  operand_left = None
  operand_right = None
  operator = None
  waiting_for = "left operand"

  counter = 0
  for element in expression:
#    print element
    if element in digits:
#	print "is a digit"
	if waiting_for == "right operand":
		operand_right = element
		solution = eval_partial(operand_left, operator, operand_right)
#		print solution
		return solution
	else:
		operand_left = element
		waiting_for = "operator"
    elif element in operators:
#	print "is an operator"
	if waiting_for == "left operand":
		operand_left = 0
	waiting_for = "right operand"
	operator = element
    elif element == '(':
#	print "bracket. Starting recursion"
	operand_right = eval(expression[counter+1:])
	solution = eval_partial(operand_left, operator, operand_right)
#	print solution
	return solution

    counter += 1



def eval_partial(operand_left, operator, operand_right):
	print "partially calculatin: " + str(operand_left) + " " + str(operator) + " " + str(operand_right)
	operand_left = int(operand_left)
	operand_right = int(operand_right)

	if operator == '-':
		return operand_left - operand_right
	else:
		return operand_left + operand_right



print eval('- (3 + ( 2 - 1 ) )')
# -4
print eval('3 + (1 + (5 + 9 ) )')
# 18
