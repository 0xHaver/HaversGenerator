import random
import string

# Create a list of all possible characters
characters = list(string.ascii_uppercase + string.digits)

# Ask the user how many codes they want to generate
num_codes = int(input("How many codes would you like to generate? "))

# Generate the specified number of unique codes
codes = []
while len(codes) < num_codes:
    # Create a new code of 16 random characters
    new_code = "".join(random.choices(characters, k=16))

    # Add hyphens every 4 characters except at the end
    new_code = "-".join(new_code[i:i+4] for i in range(0, len(new_code), 4))

    # Add the code to the list if it's not already in the list
    if new_code not in codes:
        codes.append(new_code)

# Save the codes to a file
with open("codes.txt", "w") as f:
    for c in codes:
        f.write(c + "\n")

# Print the list of codes
for c in codes:
    print(c)
