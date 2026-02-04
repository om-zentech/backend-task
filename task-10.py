'''
[Task-10]:
Pelindrome Number
'''

# Pelindrome Number

n = int(input("Enter Number: "))
temp = n  # Store number in temporary variable
rev = 0

while temp > 0: 
  last_digit = temp % 10 # It gives last digit of number
  rev = (rev*10) + last_digit # Reverse number
  temp //= 10 # Remove last digit of number and store in temporary variable

if n == rev:
  print(f'{n} is Pelindrome Number')
else:
  print(f'{n} is Not a Pelindrome Number')