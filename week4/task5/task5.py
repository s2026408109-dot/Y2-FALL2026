import random
secret = random.randint(1, 100)
attempts = 0
while attempts < 7:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Out of range.")
        continue
    attempts += 1
    if guess == secret:
        if attempts == 1:
            print("Perfect score!")
        else:
            print("Correct!")
        break
    elif guess < secret:
        print("Higher")
    else:
        print("Lower")
else:
    print("Secret number was:", secret)