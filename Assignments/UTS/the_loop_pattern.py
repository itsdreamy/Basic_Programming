row = int(input("Enter total row: "))
col = int(input("Enter total col: "))

for i in range(row):
    for j in range(col):
            end_row = row - 1
            end_col = col - 1
            middle = (end_col) // 2
            odd = row % 2 != 0 and col % 2 != 0
            even_row = row % 2 == 0 and col % 2 != 0
            even_col = col % 2 == 0
            if even_col:
                if j == 0 or j == end_col:
                    print("O", end=" ")
                elif i == 0 or i == end_row:
                    print("O", end=" ")
                else: 
                    print("H", end=" ")  
            elif even_row:
                if j == 0 or j == end_col:
                    print("O", end=" ")
                elif i == 0 or i == end_row:
                    print("O", end=" ")
                elif ((j == middle and i == middle) or (j == middle and i == (middle + 1))) :
                    print("O", end=" ")   
                else: 
                    print("H", end=" ")  

            else:  
                if i == middle and j == middle:  
                    print("O", end=" ")
    print()