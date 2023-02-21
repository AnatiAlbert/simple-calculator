#Calculator
from art_calculator import logo
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operators = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

def calculator():
  print(logo)
  num1 = float(input('What is the first number?: '))
  for operator in operators:
    print(operator)

  should_continue = True
  while should_continue:
    operation_symbol = input('Pick an operation: ')
    num2 = float(input('What is the next number?: '))
    calculation_function = operators[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')
    start_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if start_again == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()
