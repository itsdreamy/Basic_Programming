sec = float( input("Enter time in seconds: "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print(f"{sec} seconds is equal to:")
print(f"Hours   : {hours}")
print(f"Minutes : {minutes}")
print(f"Seconds : {seconds}")