# This script helps manage a single daily task with a customized reminder.

# Prompt the user for a task.
task = input("Enter your task: ").strip()
priority = input("What is the priority of this task? (high/medium/low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Use a match-case statement to create the base reminder message.
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
print("\n--- Daily Reminder ---")
print(reminder)