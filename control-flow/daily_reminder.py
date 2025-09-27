# daily_reminder.py

# Prompt user for a single task and details (exact wording expected)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

# Use a match-case statement for priority of the reminder message.
match priority:
    case 'high':
        reminder = f"High priority task, '{task}'"
    case 'medium':
        reminder = f"Medium priority task, '{task}'"
    case 'low':
        reminder = f"low priority task, '{task}'"
    case _:
        reminder = f"Reminder for your task: '{task}'(priority not specified)"

# check if the task is urgent.
if time_bound == 'yes':
    reminder += "This task requires immediate attention today!"

# Print the final reminder.
print(f"Reminder: {reminder}")