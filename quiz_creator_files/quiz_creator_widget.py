from PyQt5.QtWidgets import QTextEdit, QLineEdit, QComboBox, QPushButton, QMessageBox

class QuestionInput(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Enter the question here...")

class OptionsInput(list):
    def __init__(self):
        super().__init__()
        for label in ['A', 'B', 'C', 'D']:
            input_field = QLineEdit()
            input_field.setPlaceholderText(f"Option {label}")
            self.append(input_field)

class CorrectOptionSelector(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(['A', 'B', 'C', 'D'])

class SaveExitButtons:
    def __init__(self, question_input, option_inputs, correct_input):
        self.question_input = question_input
        self.option_inputs = option_inputs
        self.correct_input = correct_input

        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("background-color: #66bb6a; color: white; padding: 8px;")
        self.save_button.clicked.connect(self.submit_question)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setStyleSheet("background-color: #a5d6a7; padding: 6px;")
        self.exit_button.clicked.connect(self.exit_app)

    def submit_question(self):
        question = self.question_input.toPlainText().strip()
        options = [field.text().strip() for field in self.option_inputs]
        correct = self.correct_input.currentText()

        if not question or not all(options):
            QMessageBox.warning(None, "Missing Info", "Please fill in all fields.")
            return

        data = (
            f"Question: {question}\n"
            f"a) {options[0]}\n"
            f"b) {options[1]}\n"
            f"c) {options[2]}\n"
            f"d) {options[3]}\n"
            f"Correct Answer: {correct}\n"
            f"{'-' * 40}\n"
        )

        with open("quiz_creator_questions.txt", "a", encoding="utf-8") as file:
            file.write(data)

        QMessageBox.information(None, "Saved", "Question saved!")
        self.clear_fields()

    def clear_fields(self):
        self.question_input.clear()
        for field in self.option_inputs:
            field.clear()
        self.correct_input.setCurrentIndex(0)

    def exit_app(self):
        QWidget().close()
