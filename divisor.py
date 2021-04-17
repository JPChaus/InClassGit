num = (int)(input("Enter a positive numer: "))
numList = []
for i in range(1, num + 1):
    if(num % i == 0):
        numList.append(i)

print(*numList)