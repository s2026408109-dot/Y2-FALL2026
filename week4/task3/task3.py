start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
primes = []
for n in range(start, end + 1):
    if n < 2:
        continue
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print("Primes:", primes)
print("Total count:", len(primes))
print("Sum:", sum(primes))