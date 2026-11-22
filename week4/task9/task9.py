terms = int(input("Enter number of terms: "))
while terms < 1:
    terms = int(input("Enter valid term count (>= 1): "))
seq = []
a, b = 0, 1
for _ in range(terms):
    seq.append(a)
    a, b = b, a + b
print("Sequence:", *seq)
print("Sum:", sum(seq))
evens = sum(1 for x in seq if x % 2 == 0)
odds = len(seq) - evens
print("Even terms:", evens)
print("Odd terms:", odds)