username = input("Enter your username: ")

length = len(username)

if length < 5 :
    print("Username is too short!")
else :
    print(f"Username {username} is accepted!")