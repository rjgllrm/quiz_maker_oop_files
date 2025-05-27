from PyQt5.QtWidgets import QWidget, QVBoxLayout
from quiz_widgets import QuestionInput, OptionsInput, CorrectOptionSelector, SaveExitButtons

class QuizUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Creator")
        self.init_ui()

    def init_ui(self):
        self.question_input = QuestionInput()
        self.option_inputs = OptionsInput()
        self.correct_input = CorrectOptionSelector()
        self.save_button, self.exit_button = SaveExitButtons(
            self.question_input, self.option_inputs, self.correct_input
        )

        layout = QVBoxLayout()
        layout.addWidget(self.question_input)
        for field in self.option_inputs:
            layout.addWidget(field)
        layout.addWidget(self.correct_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)
