#if it's given as list or array
numbers = [8, -4, 100]

# Using loop

result = numbers[0]

for num in numbers :
    if num > result :
        result = num

print(f"The largest number is {result}")


# Using built in function
print(f"The largest number is {max(numbers)}")

# But if it's given as an input from user. it goes like this

user_input = []
biggest = 0
i = 1
while i < 4  :
    answer = int(input(f"Enter the {i} number: "))
    user_input.append(answer)
    i += 1

for number in user_input:
    if(number > biggest):
        biggest = number

print(f"the largest number is {biggest}")
