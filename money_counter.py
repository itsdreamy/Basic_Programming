try:
    total_money = int(input("Please input ur total money: "))
    moneys = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    print("\nBreakdown: ")

    for bills in moneys:
        count = total_money // bills
        if count > 0:
            print(f"{count} x {bills}")
        total_money = total_money % bills

    if total_money > 0:
        print("Masih ada sisa", total_money)

except:
    print("Please only input integer!")
