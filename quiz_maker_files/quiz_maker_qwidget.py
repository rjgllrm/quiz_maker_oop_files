from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QButtonGroup, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt
import random
from quiz_dialogs import ResultDialog, FinalDialog
from quiz_utils import load_questions

class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Time!")
        self.question_data = load_questions()

        if not self.question_data:
            QMessageBox.critical(self, "Error", "No questions found!")
            sys.exit()

        self.remaining_questions = self.question_data.copy()
        random.shuffle(self.remaining_questions)

        self.init_ui()

    def init_ui(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#f0f8ff"))
        self.setPalette(palette)

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.question_label = QLabel()
        self.question_label.setStyleSheet("font-size: 41px; font-weight: bold; color: #4caf50;")
        self.layout.addWidget(self.question_label)

        self.radio_buttons = []
        self.button_group = QButtonGroup()
        for i in range(4):
            rb = QRadioButton()
            rb.setStyleSheet("font-size: 21px; margin: 10px;")
            self.radio_buttons.append(rb)
            self.button_group.addButton(rb, i)
            self.layout.addWidget(rb)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #4caf50; font-size: 21px; color: white; padding: 5px;")
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        self.load_random_question()

    def load_random_question(self):
        if not self.remaining_questions:
            final_dialog = FinalDialog("🎉 Quiz Finished!", "finish.gif", self)
            final_dialog.exec_()
            self.close()
            return

        self.current_question = self.remaining_questions.pop()
        self.question_label.setText(self.current_question["question"])

        pixmap = QPixmap("banner.jpg")
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaled(900, 900, Qt.KeepAspectRatio))
        else:
            self.image_label.clear()

        for i, option in enumerate(self.current_question["options"]):
            self.radio_buttons[i].setText(option)
            self.radio_buttons[i].setChecked(False)

    def check_answer(self):
        selected_id = self.button_group.checkedId()
        if selected_id == -1:
            QMessageBox.warning(self, "Warning", "Please select an answer before submitting.")
            return

        selected_option = ['A', 'B', 'C', 'D'][selected_id]
        correct_option = self.current_question['correct']

        if selected_option == correct_option:
            message = f"✅ Correct! The answer is {correct_option}."
            gif_path = "correct.gif"
        else:
            message = f"❌ Wrong! The correct answer is {correct_option}."
            gif_path = "wrong.gif"

        dialog = ResultDialog(message, gif_path, self)
        dialog.exec_()
        self.load_random_question()

