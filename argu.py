import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Error: Please provide exactly two numbers as command-line arguments.")
    sys.exit(1)

try:
    # Convert arguments to numbers
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    
    # Calculate and print the sum
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
except ValueError:
    print("Error: Both arguments must be valid numbers.")
    sys.exit(1)