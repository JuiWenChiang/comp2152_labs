print("=" * 50)
print("Question 3: Coordinate System (Tuples - Creation and Unpacking)")
print("-" * 50)
# Concepts: Tuple creation, indexing, unpacking, tuple() constructor, immutability

# Create Tuples
point1 = (3, 5)
point2 = (7, 2)

# Unpack Tuples into variables
x1, y1 = point1
x2, y2 = point2

# Calculate the distance between points using the formula: 
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

# Create a tuple from the string "PYTHON" using the tuple() constructor
char_tuple=tuple("PYTHON")

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print(f"Distance between points: {distance}")
print(f"Characters tuple: {char_tuple}")
for char in char_tuple:
    print(char)

print()
