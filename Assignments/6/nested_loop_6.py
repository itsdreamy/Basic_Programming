for i in range(5):
    for j in range (5):
        if(i == j or  j==(4-i)):
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()

# * _ _ _ * 
# _ * _ * _ 
# _ _ * _ _
# _ * _ * _
# * _ _ _ *
