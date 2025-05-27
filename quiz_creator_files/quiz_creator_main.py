import sys
from PyQt5.QtWidgets import QApplication
from quiz_ui import QuizUI

def main():
    app = QApplication(sys.argv)
    window = QuizUI()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
