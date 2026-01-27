print("=" * 50)
print("Question 4: Class Attendance (Sets - Uniqueness and Operations)")
print("-" * 50)
# Concepts: Set creation, add(), remove(), union (|), intersection (&), difference (-)

monday_class =  {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")

both_class = monday_class & wednesday_class
all_students = monday_class | wednesday_class
only_monday_class = monday_class - wednesday_class
only_one_class = monday_class ^ wednesday_class

# The <= operator is used for subset comparison (less than or equal to). 
# It checks if all elements of the set on the left are present in the set on the right. 
monday_subset = monday_class <= all_students


print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {both_class}")
print(f"Attended either classes: {all_students}")
print(f"Attended Only Monday: {only_monday_class}")
print(f"Only one class (not both) : {only_one_class}")
print(f"Is Monday subset of all students? {monday_subset}")

print()