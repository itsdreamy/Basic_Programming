laptop_price = int( input("Enter your dream laptop's price: "))
monthly_saving = int( input("How much do you want to save each months? : "))

estimation = laptop_price // monthly_saving

print(f"You are {estimation} months away from taking your dream laptop home")