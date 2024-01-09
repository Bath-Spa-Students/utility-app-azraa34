#Write a program in which you can display a list of your favorite things and print the list.  

# Define a list of favorite things
favorite_things = [
    "Sunsets on the beach",  # First favorite thing
    "Books with a strong narrative",  # Second favorite thing
    "spending time with my pets",  # Third favorite thing
    "Coffee on a rainy day",  # Fourth favorite thing
    "writing diary",  # Fifth favorite thing
]

# Print the list of favorite things with detailed comments
print("My List of Favorite Things:")
print("-" * 28)  # Line to separate the header

# Use a loop to iterate through each item in the list
for index, thing in enumerate(favorite_things, start=1):
    print(f"{index}. {thing}")  # Print each favorite thing with its index

print("-" * 28)  # Line to separate the footer