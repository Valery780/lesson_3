from random import random
n = round(random() * 10)
i = 1
print("You have 3 attempts")
while i <= 3:
    x = int(input(str(i) + ' try: '))
    if x > n:
        print('Too high')
    elif x < n:
        print('Too low')
    else:
        print('You won!' % i)
        break
    i += 1
else:
    print('You lose! It was', n)