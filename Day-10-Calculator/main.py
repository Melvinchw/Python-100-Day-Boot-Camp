#create operator functions
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

#create operator dictionary
operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  #main program
  print(logo)
  num1 = float(input("What is the first number?: "))
  for symbol in operators:
    print(symbol)
  should_continue = True #This is a flag to help the while loop identify if it should start
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operators[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    user_input = input("Would you like to continue calculating? Press 'y' to continue. 'n' to start a new page.: ").lower()
    if user_input == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
"""operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number: "))
calculation_function = operators[operation_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

print("Thank you for using the calculator. Bye Bye!")"""