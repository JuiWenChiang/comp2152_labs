print("=" * 50)
print("Question 5: Contact Book (Dictionaries - Basic Operations)")
print("-" * 50)
# Concepts: Dictionary creation, accessing values, adding/modifying entries, del, keys(), values()

contacts = {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-9999"}

alice_phone = contacts["Alice"]
print(f"Alice's number: {alice_phone}")

contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after adding Bob: {contacts}")

del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

print(f"All names: {contacts.keys()}")
print(f"All numbers: {contacts.values()}")
print(f"Total contacts: {len(contacts)}")

print()