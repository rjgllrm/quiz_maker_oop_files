from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

class ResultDialog(QDialog):
    def __init__(self, message, gif_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Result")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()

        gif_label = QLabel()
        movie = QMovie(gif_path)
        gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(gif_label, alignment=Qt.AlignCenter)

        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setStyleSheet("font-size: 21px; font-weight: bold;")
        layout.addWidget(message_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)


class FinalDialog(QDialog):
    def __init__(self, message, gif_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Quiz Completed!")
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        gif_label = QLabel()
        movie = QMovie(gif_path)
        gif_label.setMovie(movie)
        movie.start()
        layout.addWidget(gif_label, alignment=Qt.AlignCenter)

        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(message_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
