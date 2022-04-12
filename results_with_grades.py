marks = int(input('Please enter your marks '))

if marks >= 75:
    print('You have passed with distinctions')
elif marks >= 60:
    print('You have passed with grade A')
elif marks >= 45:
    print('You have passed with grade B')
elif marks >= 40:
    print('You have passed with grade C')
else:
    print('You have failed')