# Define the base price per square foot
base_price_per_sqft = 0.5

# Get user input for square feet of cleaning area
cleaning_area = float(input("Enter the square feet of cleaning area: "))

# Get user input for cleaning services needed
cleaning_services = input("Enter the cleaning services needed: ")

# Calculate the total price based on the cleaning area and services needed
total_price = base_price_per_sqft * cleaning_area

# Apply additional charges based on the cleaning services needed
if "deep cleaning" in cleaning_services:
    total_price += 50
if "carpet cleaning" in cleaning_services:
    total_price += 30

# Display the final price to the user
print("The final price for the cleaning job is: $", total_price)
