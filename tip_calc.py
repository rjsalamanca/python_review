bill = int(input('Total bill amount? '))
level_of_service = input('Level of service? ')
tip = 0

if level_of_service == 'good':
    tip = bill * .2
elif level_of_service == 'fair':
    tip = bill * .15
elif level_of_service == 'bad':
    tip = bill * .10

total = bill + tip

print('Tip amount: $%.2f' % tip)
print('Total amount: $%.2f' % total)