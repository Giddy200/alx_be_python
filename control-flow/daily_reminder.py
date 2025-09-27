# daily_reminder.py

# Prompt the user for a single task, its priority, and if it's time-bound.
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate reminder using match-case for priority.
match priority:
    case "high":
        reminder = f"High priority task, '{task}'"
    case "medium":
        reminder = f"Medium priority task, '{task}'"
    case "low":
        reminder = f"Low priority task, '{task}'"
    case _:
        reminder = f"Task: '{task}' (priority not specified)"

# Add the time-bound message if applicable.
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Display the final reminder.
print(f"Reminder:{reminder}")