import string
import random

num = (int)(input("Enter a positive numer: "))
characters = string.ascii_letters + string.digits
print(''.join(random.choice(characters) for i in range(num)))