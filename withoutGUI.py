
ichara_thesign = input('give your expression :')

num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))

if ichara_thesign == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

elif ichara_thesign == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

elif ichara_thesign == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

elif ichara_thesign == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

else:
    print('error')
