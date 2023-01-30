import random
n = int(input("Enter a random number: "))
randomL = []
for i in range(n):
    number = random.randint(1, 70)
    while number in randomL:
        number = random.randint(1, 70)
    randomL.append(number)

print(randomL)

