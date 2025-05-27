import sys
from PyQt5.QtWidgets import QApplication
from quiz_window import QuizWindow

def main():
    app = QApplication(sys.argv)
    quiz = QuizWindow()
    quiz.resize(850, 900)
    quiz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
