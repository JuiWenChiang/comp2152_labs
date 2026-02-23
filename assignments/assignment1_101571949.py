# Author: Jui-Wen Chiang
# Assignment: #1

print("=" * 50)


# Task B
gym_member = "Alex Alliton"  # Text type: str
preferred_weight_kg = 20.5  # Numeric type: float
highest_reps = 25  # Numeric type: int
membership_active = True  # Boolean type: bool


# Task C
# A dictionary with string key and tuple value
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (42, 90, 15),
    "Taylor": (63, 38, 34),
    "Wendy": (80, 20, 12),
    "Roxy": (64, 92, 28),
}


# Task D
totals = {}
for key in workout_stats:
    totals[f"{key}_Total"] = sum(workout_stats[key])

workout_stats.update(totals)


# Task E
# workout_list is a 2D list containing workout minutes for each friend (row) across yoga, running, and weightlifting (column)
workout_list = []
for minTuple in workout_stats.values():
    if type(minTuple) is tuple:
        workout_list.append(list(minTuple))


# Task F
all_yoga_running_minutes = []
last_two_weightlifting_minutes = []

length = len(workout_list)
index = 0
for minList in workout_list:
    index += 1
    all_yoga_running_minutes.append(minList[:2])
    if index >= length - 1:
        last_two_weightlifting_minutes.append(minList[2])

print(f"Minutes of Yoga and Running for all friends: {all_yoga_running_minutes}")
print(f"Weightlifting for last two friends: {last_two_weightlifting_minutes}")
print("")


# Task G
for item in workout_stats:
    mins = workout_stats[item]
    if type(mins) is not tuple and mins >= 120:
        name = item.replace("_Total", "")
        print(f"Great job staying active, {name}!")

print("")


# Task H
activity = ["Yoga", "Running", "Weightlifting"]
activity_index = 0
name = input("Enter a name to search: ")
if name in workout_stats:
    print("Name", name)
    mins = workout_stats[name]
    for val in mins:
        print(f"{activity[activity_index]}: {val} minutes")
        activity_index += 1
    total_val = workout_stats[f"{name}_Total"]
    print("Total workout minutes", total_val)
else:
    print(f"Friend {name} not found in the records.")

print("")


# Task I
friend_totals = {}
for key in workout_stats:
    if key.endswith("_Total"):
        val = workout_stats[key]
        friend_name = key.replace("_Total", "")
        friend_totals[friend_name] = val

highest_friend = max(friend_totals, key=friend_totals.get)
highest_min = friend_totals[highest_friend]
lowest_friend = min(friend_totals, key=friend_totals.get)
lowest_min = friend_totals[lowest_friend]
print(f"{highest_friend} with the highest total workout minutes: {highest_min}")
print(f"{lowest_friend} with the lowest total workout minutes: {lowest_min}")

print("")
print("=" * 50)
