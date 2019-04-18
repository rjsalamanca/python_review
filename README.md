# python_review

## Day of the Week

**Solution is stored in: day_of_week.py**

Given the following code that prompts the user for a day number (the int function converts a numeric string to a number):
```
day = int(input('Day (0-6)? '))

# Fill in your code here
```

The user will enter a number between 0 to 6 inclusive. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on. Here's an example user session (this assumes you've named the file day_of_week.py):

```
$ python day_of_week.py
Day (0-6)? 5
Friday
$ python day_of_week.py
Day (0-6)? 0
Sunday
```

## Work or Sleep In?

**Solution is stored in: work_or_sleep_in.py**

Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:

```
$ python work_or_sleep_in.py
Day (0-6)? 5
Go to work
$ python work_or_sleep_in.py
Day (0-6)? 6
Sleep in
```

## Celsius to Fahrenheit

**Solution is stored in: degree_conversion.py**

Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user. Example session:

```
$ python degree_conversion.py
Temperature in C? 28
82.4 F
$ python degree_conversion.py
Temperature in C? -5
23 F
```

Hint: the formula to convert degrees C to degrees F is: F = C x 1.8 + 32.

## Tip Calculator

**Solution is stored in: tip_calc.py**

Prompt the user for two things:

1. The total bill amount
2. The level of service, which can be one of the following: good, fair, or bad

Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

- good -> 20%
- fair -> 15%
- bad -> 10%

Example session:
```
$ python tip_calc.py
Total bill amount? 100
Level of service? good
Tip amount: $20.00
Total amount: $120.00
$ python tip_calc.py
Total bill amount? 48
Level of service? bad
Tip amount: $4.80
Total amount: $52.80
```

Hints:

- Remember that you need to convert the input from the user input to floats instead of ints. Use the float function instead of the int function.
- To format a float number as a dollar value, use Python's formatting syntax: '%.2f' % amount

## Tip Calculator 2

**Solution is stored in: tip_calc2.py**

Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:
```
$ python tip_calc2.py
Total bill amount? 100
Level of service? good
Split how many ways? 5
Tip amount: $20.00
Total amount: $120.00
Amount per person: $24.00
```