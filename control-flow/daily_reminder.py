# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound.lower() == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it soon."
        print(reminder)
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound.lower() == "yes":
            reminder += " that requires attention today."
        else:
            reminder += ". You can complete it when you have time."
        print(reminder)
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound.lower() == "yes":
            reminder += ", but it is time-bound. Try to complete it today."
        else:
            reminder += ". Consider completing it when you have free time."
        print(reminder)