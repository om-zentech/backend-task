'''
Task-14:
Find LCM and GCD of a number
'''

# define a function for finding LCM and GCD of two numbers
def lcm_gcd():
    while True:
        try:
            num_a = int(input('Enter Number 1: '))
            num_b = int(input('Enter Number 2: '))
            break
        except ValueError:
            print('Invalid input try again!')
    num_a_copy = num_a
    num_b_copy = num_b
    while num_b != 0:
        num_a,num_b = num_b,num_a%num_b # this line assigns num_b to num_a and num_a%num_b until num_b becomes 0
    print(f'GCD is: {num_a}')
    
    lcm_of_number = (num_a_copy*num_b_copy)//num_a # LCM can be calculated using GCD
    print(f'LCM is: {lcm_of_number}')

lcm_gcd()