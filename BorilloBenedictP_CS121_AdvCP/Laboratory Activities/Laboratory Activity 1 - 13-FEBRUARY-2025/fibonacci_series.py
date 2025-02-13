num = int(input("Enter the number of terms: "))
first = 0
second = 1
temp = 0

print("Fibonacci Series:", end=" ")
for i in range(num):
    print(first, end=" ")
    temp = second
    second = first + second
    first = temp
