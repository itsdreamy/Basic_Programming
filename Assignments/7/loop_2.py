for i in range(4):
    for j in range(5):
        if j == 2 and (i == 0 or i == 3):
            print("0", end=" ")
        elif (i != 0 and i != 3) and (j >= 1 and j <= 3):
            print("0", end=" ")
        else:
            print("X", end=" ")
    print()

#Note: Idk why, but in the example the rows are 4 and cols are 5
# X X 0 X X 
# X 0 0 0 X 
# X 0 0 0 X 
# X X 0 X X 