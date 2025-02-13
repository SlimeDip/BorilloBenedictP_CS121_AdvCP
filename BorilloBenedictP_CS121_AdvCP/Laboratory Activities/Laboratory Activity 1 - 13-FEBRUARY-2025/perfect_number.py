num = int(input("Enter a number: "))
ans = 0

for i in range(1, num):
    if num % i == 0:
        ans += i

if num == ans:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")