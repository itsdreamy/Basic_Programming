Numbers = [1, 5, 7, 8, 10, 18, 50, 30]
counting = len(Numbers)

count = 0

for num in Numbers:
    if num % 2 == 0:
        count += 1

print(f"The amount of even number in the array is {count}")

