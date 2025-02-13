num = int(input("Enter a number: "))
first = 0
second = 1
temp = 0

print("Fibonacci Series:", end=" ")
for i in range(num+2):
    print(first, end=" ")
    temp = second
    second = first + second
    first = temp
