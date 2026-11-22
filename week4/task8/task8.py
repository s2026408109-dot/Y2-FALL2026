stock = 100
sold = 0
while stock > 0:
    q = int(input("Enter quantity sold (-1 to stop): "))
    if q == -1:
        break
    if q <= 0:
        print("Error: Invalid quantity.")
        continue
    if q > stock:
        print("Error: Exceeds available stock.")
        continue
    stock -= q
    sold += q
print("Total units sold:", sold)
print("Remaining stock:", stock)