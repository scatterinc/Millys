from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox

from generated.Ui_MainWindow import Ui_MainWindow
from ui.CreateCompanyDialog import CreateCompanyDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from the designer.
        self.setupUi(self)
        self.setFixedSize(self.size())

        # Center window on screen.
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def action_new_triggered(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setMaximumWidth(500)
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure you want to create a new entity?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.buttonClicked.connect(self.dialog_button_clicked)
        msg_box.exec()

    def dialog_button_clicked(self, i):
        if i.text() == '&Yes':
            ui = CreateCompanyDialog(parent=self)
            ui.show()

    @staticmethod
    def action_open_triggered():
        print("Action open triggered.")

    @staticmethod
    def action_exit_triggered():
        exit(0)
