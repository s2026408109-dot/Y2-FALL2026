marks = []
passed = 0
failed = 0
for i in range(10):
    m = float(input(f"Enter marks for student {i+1}: "))
    while m < 0 or m > 100:
        m = float(input("Invalid. Enter marks between 0 and 100: "))
    marks.append(m)
    if m >= 50:
        passed += 1
    else:
        failed += 1
    if m >= 90:
        print("Grade: A")
    elif m >= 80:
        print("Grade: B")
    elif m >= 70:
        print("Grade: C")
    elif m >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
print("Passed:", passed)
print("Failed:", failed)
print("Highest mark:", max(marks))
print("Class average:", sum(marks) / len(marks))