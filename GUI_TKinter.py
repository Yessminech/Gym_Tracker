import tkinter as tk
from datetime import datetime

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def open_exercise_window(workout_window):
    clear_window(workout_window) 
    exercise_label = tk.Label(workout_window, text="Exercise:")
    exercise_entry = tk.Entry(workout_window)
    sets_label = tk.Label(workout_window, text="Sets:")
    sets_entry = tk.Entry(workout_window)
    reps_label = tk.Label(workout_window, text="Reps:")
    reps_entry = tk.Entry(workout_window)

    def done():
        clear_window(workout_window)
        success_label = tk.Label(workout_window, text="Exercise added successfully!")
        add_another_button = tk.Button(workout_window, text="Add Another Exercise", command=lambda: open_exercise_window(workout_window))  
        close_button = tk.Button(workout_window, text="Close", command=workout_window.destroy)
        success_label.pack()
        add_another_button.pack()
        close_button.pack()

    done_button = tk.Button(workout_window, text="Done", command=done)

    exercise_label.pack()
    exercise_entry.pack()
    sets_label.pack()
    sets_entry.pack()
    reps_label.pack()
    reps_entry.pack()
    done_button.pack()

## Add workout window
def open_workout_window(welcome_window):
    clear_window(welcome_window) 
    date_label = tk.Label(welcome_window, text="Date:")
    day_var = tk.StringVar(welcome_window, value=str(datetime.now().day))  # Convert the day to a string
    month_var = tk.StringVar(welcome_window, value=str(datetime.now().month))  # Convert the month to a string
    day_menu = tk.OptionMenu(welcome_window, day_var, *range(1, 32))
    month_menu = tk.OptionMenu(welcome_window, month_var, *range(1, 13))
    year_menu = tk.OptionMenu(welcome_window, tk.StringVar(welcome_window), *range(2020, 2036))
    location_label = tk.Label(welcome_window, text="Location:")
    location_entry = tk.Entry(welcome_window)
    duration_label = tk.Label(welcome_window, text="Duration:")
    duration_var = tk.StringVar(welcome_window)
    duration_var.set("20")  # default value
    duration_options = ["20", "40", "60"]
    duration_menu = tk.OptionMenu(welcome_window, duration_var, *duration_options)
    add_exercise_button = tk.Button(welcome_window, text="Add Exercise", command=lambda: open_exercise_window(welcome_window)) 

    date_label.pack()
    day_menu.pack(side="left")
    month_menu.pack(side="left")
    year_menu.pack(side="left")
    location_label.pack()
    location_entry.pack()
    duration_label.pack()
    duration_menu.pack()
    add_exercise_button.pack()

## Welcome window
main_window = tk.Tk()

welcome_label = tk.Label(main_window, text="Welcome to the Workout Tracker!")
welcome_label.pack()

add_workout_button = tk.Button(main_window, text="Add Workout", command=lambda: open_workout_window(main_window)) ##lambda is used to pass arguments to the function
add_workout_button.pack()

main_window.mainloop()
