row = 8
col = 7

for i in range(row):
    for j in range(col):
            end_row = row - 1
            end_col = col - 1
            middle = (end_col) // 2
            if row % 2 != 0 and col % 2 != 0:
                if j == 0 or j == (end_col):
                    print("O", end=" ")
                elif i == 0 or i == (end_row):
                    print("O", end=" ")
                elif i == j == ((end_row)/2):
                    print("O", end=" ")                     
                else: 
                    print("H", end=" ")    
            elif row % 2 == 0:    
                if j == 0 or j == (end_col):
                    print("O", end=" ")
                elif i == 0 or i == (end_row):
                    print("O", end=" ")
                elif ((j == middle and i == middle) or (j == middle and i == (middle + 1))) :
                    print("O", end=" ")                     
                else: 
                    print("H", end=" ")  
            elif col % 2 == 0 and row % 2 != 0:    
                if j == 0 or j == (end_col):
                    print("O", end=" ")
                elif i == 0 or i == (end_row):
                    print("O", end=" ")                 
                else: 
                    print("H", end=" ")        
    print()