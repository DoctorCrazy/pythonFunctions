class Calculator:
    def addition(self):
        return num1 + num2
    def subtraction(self):
        return num1 - num2
    def multiplication(self):
        return num1 * num2
    def division(self):
        return num1 / num2

num1 = int(input('First Number>>> '))
num2 = int(input('Second Number>>> '))
operator = input('Operator>>> ')

action = Calculator()
if operator == '+':
    print(action.addition())
elif operator == '-':
    print(action.subtraction())
elif operator == '*':
    print(action.multiplication())
elif operator == '/':
    print(action.division())
else:
    print('Bad Operator!!')