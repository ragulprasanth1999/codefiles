import re

def is_valid_vanity_plate(plate):
    # Define a regex pattern for a valid vanity plate
    pattern = r'^[A-Z]{2}[A-Z0-9]{0,4}[1-9A-Z]$'

    # Use re.match to check if the plate matches the pattern
    match = re.match(pattern, plate)

    # Check if the first number is not '0' and the plate is valid
    if match:
        return True
    else:
        return False

# Example usage:
vanity_plate = input("Enter a vanity plate: ")

if is_valid_vanity_plate(vanity_plate):
    print("Valid",end="")
else:
    print("Invalid",end="")

def is_valid_vanity_plate(plate):
    # Define a regex pattern for a valid vanity plate
    pattern = r'^[A-Z]{2}[A-Z0-9]*[1-9A-Z]$'

    # Use re.match to check if the plate matches the pattern
    match = re.match(pattern, plate)

    # Check if the first character is not '0' and the plate is valid
    if match and plate[2] != '0':
        return True
    else:
        return False

# Example usage:
vanity_plate = input("Enter a vanity plate: ")

if is_valid_vanity_plate(vanity_plate):
    print("Valid")
else:
    print("Invalid")
import re

def is_valid_vanity_plate(plate):
    # Define a regex pattern for a valid vanity plate
    pattern = r'^[A-Z]{2}[1-9A-Z][A-Z0-9]{0,3}$'

    # Use re.match to check if the plate matches the pattern
    match = re.match(pattern, plate)

    # Check if the first character is not '0' and the plate is valid
    if match:
        return True
    else:
        return False

# Example usage:
vanity_plate = input("Enter a vanity plate: ")

if is_valid_vanity_plate(vanity_plate):
    print("Valid vanity plate.")
else:
    print("Invalid vanity plate.")
