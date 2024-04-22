from Workout import Workout
from Exercise import Exercise
import pandas as pd

# Create a new workout

# Get Workout details from user 
date = input("Enter the date of the workout: ")
duration = int(input("Enter the duration of the workout: "))
location = input("Enter the location of the workout: ")
exercice_count = int(input("How many exercises you have done today?"))
exercices = []
workout = Workout(date, location, duration, exercices)

# Get exercices details from user 
for _ in range(exercice_count):
    name = input("Enter the name of the exercise: ")
    exercice_type = input("Enter the type of the exercise: ")
    duration = int(input("Enter the duration of the exercise: "))
    repetitions = int(input("Enter the repetitions of the exercise: "))
    sets = int(input("Enter the sets of the exercise: "))
    exercice = Exercise(name, exercice_type, sets, repetitions)
    exercices.append(exercice)
    
    # Create a DataFrame to store the workout data
    workout_data = {
        'Exercise Name': [],
        'Exercise Type': [],
        'Sets': [],
        'Repetitions': [],
        'Duration': []
    }

    # Add workout data to the DataFrame
    for exercise in exercices:
        workout_data['Exercise Name'].append(exercise.name)
        workout_data['Exercise Type'].append(exercise.exercice_type)
        workout_data['Sets'].append(exercise.sets)
        workout_data['Repetitions'].append(exercise.repetitions)

## This is not working 
    # Create a DataFrame from the workout data
    df = pd.DataFrame(workout_data)

    # Export the DataFrame to a CSV file
    filename = f"/home/yessmine/projects/gymTracker/workout_{workout.date}.csv"
    df.to_csv(filename, index=False)