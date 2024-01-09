#Write a program to take 5 numbers as an input from the user and print the sum and average

# Initialize variables to store the sum and count of numbers
sum_of_numbers = 0
count_of_numbers = 0

# Use a loop to take 5 numbers as input
for i in range(5):
    # Prompt the user for input and convert the input to a float
    user_input = float(input(f"Enter number {i + 1}: "))
    
    # Add the input to the sum
    sum_of_numbers += user_input
    
    # Increment the count of numbers
    count_of_numbers += 1

# Calculate the average by dividing the sum by the count
average_of_numbers = sum_of_numbers / count_of_numbers

# Print the sum and average with detailed comments
print("\nSum of the numbers:", sum_of_numbers)  # Display the sum
print("Average of the numbers:", average_of_numbers)  # Display the average