import sys
import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.datepicker import DatePicker
from datetime import date

class WorkoutTracker(App):
    def build(self):
        self.title = "Workout Tracker"
        layout = BoxLayout(orientation='vertical')
        self.current_layout = layout
        self.show_welcome_screen()
        return layout

    def show_welcome_screen(self):
        self.clear_layout()
        welcome_label = Label(text="Welcome to the Workout Tracker!", font_size=20, color=(0, 0, 1, 1))
        self.current_layout.add_widget(welcome_label)
        add_workout_button = Button(text="Add Workout", background_color=(0, 1, 0, 1), color=(1, 1, 1, 1))
        add_workout_button.bind(on_press=self.show_workout_dialog)
        self.current_layout.add_widget(add_workout_button)

    def show_workout_dialog(self, instance):
        layout = BoxLayout(orientation='vertical')
        dialog = Popup(title="Add Workout", content=layout, size_hint=(None, None), size=(400, 400))
        
        date_label = Label(text="Date:")
        date_edit = DatePicker(date=date.today())
        layout.add_widget(date_label)
        layout.add_widget(date_edit)

        location_label = Label(text="Location:")
        location_entry = TextInput()
        layout.add_widget(location_label)
        layout.add_widget(location_entry)

        duration_label = Label(text="Duration:")
        duration_combo = Spinner(values=["20", "40", "60"])
        layout.add_widget(duration_label)
        layout.add_widget(duration_combo)

        add_exercise_button = Button(text="Add Exercise", background_color=(1, 0.5, 0, 1), color=(1, 1, 1, 1))
        add_exercise_button.bind(on_press=dialog.dismiss)
        add_exercise_button.bind(on_release=lambda instance: self.show_exercise_dialog(date_edit.date, location_entry.text, duration_combo.text))
        layout.add_widget(add_exercise_button)

        dialog.open()

    def show_exercise_dialog(self, workout_date, location, duration):
        layout = BoxLayout(orientation='vertical')
        dialog = Popup(title="Add Exercise", content=layout, size_hint=(None, None), size=(400, 400))

        exercise_label = Label(text="Exercise:")
        exercise_entry = TextInput()
        layout.add_widget(exercise_label)
        layout.add_widget(exercise_entry)

        sets_label = Label(text="Sets:")
        sets_entry = TextInput()
        layout.add_widget(sets_label)
        layout.add_widget(sets_entry)

        reps_label = Label(text="Reps:")
        reps_entry = TextInput()
        layout.add_widget(reps_label)
        layout.add_widget(reps_entry)

        done_button = Button(text="Done", background_color=(0.5, 0, 0.5, 1), color=(1, 1, 1, 1))
        done_button.bind(on_press=dialog.dismiss)
        done_button.bind(on_release=lambda instance: self.show_success_screen())
        layout.add_widget(done_button)

        dialog.open()

    def show_success_screen(self):
        self.clear_layout()
        success_label = Label(text="Exercise added successfully!", font_size=18, color=(0, 1, 0, 1))
        self.current_layout.add_widget(success_label)

        add_another_button = Button(text="Add Another Exercise", background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        add_another_button.bind(on_press=self.show_exercise_dialog)
        self.current_layout.add_widget(add_another_button)

        close_button = Button(text="Close", background_color=(1, 0, 0, 1), color=(1, 1, 1, 1))
        close_button.bind(on_press=self.stop)
        self.current_layout.add_widget(close_button)

    def clear_layout(self):
        self.current_layout.clear_widgets()

if __name__ == "__main__":
    WorkoutTracker().run()
