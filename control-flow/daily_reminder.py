# A script that draws a text-based square pattern of asterisks.
# Prompt the user for a task.
task = input("What is the task for today? ")

# Prompt for priority (high, medium, low).
priority = input("What is the priority of this task? (high/medium/low): ").lower()

# Prompt if the task is time-bound.
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder for your {priority} priority task: {task}."

# Use a match-case statement to create the base reminder message.
match priority:
    case 'high':
        reminder = f"Urgent Reminder: Your high priority task, '{task}', needs attention!"
    case 'medium':
        reminder = f"Friendly Reminder: Your medium priority task, '{task}', is waiting for you."
    case 'low':
        reminder = f"Note: Your low priority task, '{task}', can be done at your convenience."
    case _:
        reminder = f"Reminder for your task: {task}."

# Add the time-bound message if applicable.
if time_bound == 'yes':
    reminder += " ⚡ This task requires immediate attention today!"

# Display the final reminder.
print("\n--- Daily Reminder ---")
print(reminder)