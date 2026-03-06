number = []

for i in range(3):
    num = int( input(f"Enter the {i + 1} number: "))
    number.append(num)

largest = number[0]
for num in number:
    if num > largest:
        largest = num

printNum = number[0:]

print(f"{largest} is the largest number among {printNum}")