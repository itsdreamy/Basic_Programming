# using while
i = 1

while i <= 50 : 
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} is FizzBuzz")
    elif i % 5 == 0:
        print(f"{i} is Buzz")
    elif i % 3 == 0:
        print(f"{i} is Fizz")
    else:
        print(i)

    i += 1

# using for loop
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is FizzBuzz")
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")
    else:
        print(num)
