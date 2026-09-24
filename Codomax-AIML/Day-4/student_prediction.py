# Simple Machine Learning-style logic example
# This is NOT a trained ML model.
# It is only a simple rule-based example.

hours = float(input("Enter hours studied: "))

if hours >= 6:
    prediction = "High chance of good performance"
elif hours >= 3:
    prediction = "Moderate chance of good performance"
else:
    prediction = "Needs more study"

print("Prediction:", prediction)