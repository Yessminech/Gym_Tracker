class Workout:
    def __init__(self, date, location, duration, exercises):
        self.date =date
        self.location = location
        self.duration = duration
        self.exercises = exercises
        
        
# def export_to_csv(self, workout_date, location, duration, exercise, sets, reps):
#     with open('workout_data.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([workout_date, location, duration, exercise, sets, reps])
