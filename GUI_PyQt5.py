import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout, QComboBox, QDateEdit, QDialog
from PyQt5.QtGui import QColor
from datetime import date

class WorkoutTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Workout Tracker")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.current_layout = None
        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_layout()
        welcome_label = QLabel("Welcome to the Workout Tracker!")
        welcome_label.setStyleSheet("font-size: 20px; color: blue;")
        self.layout.addWidget(welcome_label)
        add_workout_button = QPushButton("Add Workout")
        add_workout_button.setStyleSheet("background-color: green; color: white;")
        add_workout_button.clicked.connect(self.show_workout_dialog)
        self.layout.addWidget(add_workout_button)

    def show_workout_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Workout")
        layout = QFormLayout(dialog)

        date_label = QLabel("Date:")
        date_edit = QDateEdit(date.today())
        layout.addRow(date_label, date_edit)

        location_label = QLabel("Location:")
        location_entry = QLineEdit()
        layout.addRow(location_label, location_entry)

        duration_label = QLabel("Duration:")
        duration_combo = QComboBox()
        duration_combo.addItems(["20", "40", "60"])
        layout.addRow(duration_label, duration_combo)

        add_exercise_button = QPushButton("Add Exercise")
        add_exercise_button.setStyleSheet("background-color: orange; color: white;")
        add_exercise_button.clicked.connect(dialog.accept)
        layout.addRow(add_exercise_button)

        if dialog.exec_() == QDialog.Accepted:
            self.show_exercise_dialog(date_edit.date().toPyDate(), location_entry.text(), duration_combo.currentText())

    def show_exercise_dialog(self, workout_date, location, duration):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Exercise")
        layout = QFormLayout(dialog)

        exercise_label = QLabel("Exercise:")
        exercise_entry = QLineEdit()
        layout.addRow(exercise_label, exercise_entry)

        sets_label = QLabel("Sets:")
        sets_entry = QLineEdit()
        layout.addRow(sets_label, sets_entry)

        reps_label = QLabel("Reps:")
        reps_entry = QLineEdit()
        layout.addRow(reps_label, reps_entry)

        done_button = QPushButton("Done")
        done_button.setStyleSheet("background-color: purple; color: white;")
        done_button.clicked.connect(dialog.accept)
        layout.addRow(done_button)

        if dialog.exec_() == QDialog.Accepted:
            self.show_success_screen()
#            self.export_to_csv(workout_date, location, duration, exercise_entry.text(), sets_entry.text(), reps_entry.text())

    def show_success_screen(self):
        self.clear_layout()
        success_label = QLabel("Exercise added successfully!")
        success_label.setStyleSheet("font-size: 18px; color: green;")
        self.layout.addWidget(success_label)

        add_another_button = QPushButton("Add Another Exercise")
        add_another_button.setStyleSheet("background-color: blue; color: white;")
        add_another_button.clicked.connect(self.show_exercise_dialog)
        self.layout.addWidget(add_another_button)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("background-color: red; color: white;")
        close_button.clicked.connect(self.close)
        self.layout.addWidget(close_button)

    def clear_layout(self):
        if self.current_layout:
            while self.current_layout.count():
                child = self.current_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorkoutTracker()
    window.show()
    sys.exit(app.exec_())