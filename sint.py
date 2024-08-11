# manual_grid_val_test.py

import sys

# Check if an argument is provided
if len(sys.argv) > 1:
    # Get the argument passed (assuming it's numeric)
    try:
        argument = int(sys.argv[1])  # Convert the argument to an integer
        # Now you can use 'argument' in your script logic
        print(f"Argument passed to the script: {argument}")
        
        # Example: Perform some action based on the argument
        # Replace this with your actual script logic
        result = argument * 2
        print(f"Result of some operation: {result}")
        
    except ValueError:
        print("Error: Argument must be an integer.")
else:
    print("Error: Missing argument. Please provide an integer.")
