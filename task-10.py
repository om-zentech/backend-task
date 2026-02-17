'''
[Task-10]:
Pelindrome Number
'''

# Pelindrome Number
def is_pelindrome():
  while True:
    try:      
      number = int(input("Enter Number: "))
      if number < 0:
        print('Negative Number does not have a Pelindrome Number')
        continue
      break
    except ValueError:
      print("Invalid input. Please enter an integer.")
      continue
  copy_of_number = number  # Store number in temporary variable
  reverse = 0

  while copy_of_number > 0: 
    last_digit = copy_of_number % 10 # It gives last digit of number
    reverse = (reverse*10) + last_digit # Reverse number
    copy_of_number //= 10 # Remove last digit of number and store in temporary variable

  if number == reverse:
    return f'{number} is Pelindrome Number'
  else:
    return f'{number} is Not a Pelindrome Number'

print(is_pelindrome())