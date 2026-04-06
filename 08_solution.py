password = 'abhi'

pass_len = len(password)

if pass_len <6:
    strength = 'Week'
elif pass_len <=10:
    strength = 'Medium'
else:
    strength = 'strong'
print('Password strength is: ', strength)