# Day 4 - Functions and Lists

# Function
def greet(name):
    print("Hello", name)


greet("Vishal")


# Function with return value
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Sum:", result)


# List
marks = [85, 90, 78, 92, 88]

print("\nMarks:", marks)
print("First mark:", marks[0])
print("Number of marks:", len(marks))


# Add an element
marks.append(95)

print("Updated marks:", marks)


# Loop through list
print("\nAll marks:")

for mark in marks:
    print(mark)


# Calculate average
average = sum(marks) / len(marks)

print("Average:", average)