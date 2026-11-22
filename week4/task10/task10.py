pos = []
evens = 0
odds = 0
while True:
    n = int(input("Enter an integer (0 to stop): "))
    if n == 0:
        break
    if n < 0:
        continue
    pos.append(n)
    if n % 2 == 0:
        evens += 1
    else:
        odds += 1
if pos:
    print("Even numbers:", evens)
    print("Odd numbers:", odds)
    print("Largest positive:", max(pos))
    print("Sum:", sum(pos))
    print("Average:", sum(pos) / len(pos))
else:
    print("No positive numbers entered.")