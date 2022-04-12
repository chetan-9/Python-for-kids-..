'''     Simple Calculator

It is a simple calculator which takes user inputs, performs arithmetic instructions
and output results to the screen.

v1   7/2/2022   Initial draft
v2   9/2/2022   Added comments to make prgram more readable

'''

# Accept two numbers from user
x = int(input('Enter first number '))
y = int(input('Enter second number '))

print('Value of x = ', x)
print('Value of y = ', y)

# Performs arithmetic operations and prints result
sum_val = x + y
print('Addition of two given number = ', sum_val)

diff_val = x - y
print('Diffrence of two given number = ', diff_val)

prod_val = x * y
print('Product of two given numbers = ', prod_val)

div_val = x / y
print('Division of two given numbers = ', div_val)
