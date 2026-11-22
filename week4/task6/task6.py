total_revenue = 0
while True:
    units = float(input("Enter units consumed (-1 to stop): "))
    if units == -1:
        break
    if units < 0:
        print("Invalid units.")
        continue
    bill = 0
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = 100 * 10 + (units - 100) * 15
    elif units <= 300:
        bill = 100 * 10 + 100 * 15 + (units - 200) * 20
    else:
        bill = 100 * 10 + 100 * 15 + 100 * 20 + (units - 300) * 25
    total_revenue += bill
    print("Bill:", bill)
print("Total revenue:", total_revenue)