numbers =  [9, 100, 101, 88, 3, 7]

#easy way
numbers.sort()
second = numbers[-2]
print(f"The second largest number is {second}")

#loop way
largest = 0
second_largest = 0

for num in numbers:
    if num > largest :
        second_largest = largest
        largest = num
    elif num < largest and num > second_largest:
        second_largest = num

print(f"The second largest number is {second_largest}")