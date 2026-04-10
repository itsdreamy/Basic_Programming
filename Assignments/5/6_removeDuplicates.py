raw_numbers = [1,1,2,2,4,4,5,6]

numbers = []

for num in raw_numbers:
    if num not in numbers:
        numbers.append(num)
    
print(numbers)