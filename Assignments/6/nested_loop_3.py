for index, i in enumerate(range(10, 5, -2)):
    for j in range(9-index, 4, -1) :
        print(f"{i} * {j} = {i * (j)}")
        i -= 1
    print()