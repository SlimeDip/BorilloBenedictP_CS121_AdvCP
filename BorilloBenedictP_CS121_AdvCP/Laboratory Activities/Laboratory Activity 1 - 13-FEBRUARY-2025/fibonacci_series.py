num = int(input("Enter a number: "))
first = 0
second = 1
temp = 0

if num == 1:
    print("Fibonacci Series: 0")
elif num == 2:
    print("Fibonacci Series: 0 1")
elif num >= 3:
    print("Fibonacci Series: 0 1", end=" ")
    for i in range(num-2):
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
else:
    print("Invalid number")