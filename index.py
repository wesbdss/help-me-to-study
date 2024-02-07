from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("HELP ME STUDY")
        button = QPushButton("sai fora")
        self.setCentralWidget(button)
    
window = MainWindow()

window.show()


app.exec()