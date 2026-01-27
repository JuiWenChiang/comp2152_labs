print("=" * 50)
print("Question 1 : Student Grade List (Lists - Basic Operations)")
print("-" * 50)
# Concepts: List creation, append(), sort(), len(), indexing

grade = [85, 92, 78, 95, 88]
grade.append(90)
grade.sort()

print(f"Sort grades : {grade}")
print(f"Hightest grade : {grade[-1]}")
print(f"Lowest grade : {grade[0]}")
print(f"Totle number of grades : {len(grade)}")
print()