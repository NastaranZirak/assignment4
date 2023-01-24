N = int(input("please enter n = "))
f = 1
s = 1
sum = 2
counted = 1
print("The series is: ", end = " ")

while(counted <= N):
    counted += 1
    print(f, end=" ")
    f = s
    s = sum
    sum = f + s

