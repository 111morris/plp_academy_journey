num_1 = int(input('Enter your first integer number: '))
num_2 = int(input('Enter your second integer number: '))

operation = input('Enter operation (+, -, *, /): ')

if operation == '+': 
    result = num_1 + num_2
elif operation == '-':
   result = num_1 - num_2 
elif operation == '*':
    result = num_1 * num_2
elif operation == '/':
    if num_2 !=0: 
        result = num_1/num_2
    else: 
        print('Division failed')
else: 
    print('You\'ve entered invalid operation. ')

print(num_1, operation, num_2,'=', result)
