# Day 3 - Conditions and Loops

# If-else
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# For loop
print("\nNumbers from 1 to 5:")

for i in range(1, 6):
    print(i)


# While loop
print("\nCountdown:")

count = 5

while count > 0:
    print(count)
    count = count - 1

print("Done!")