from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDialog, QFormLayout, QLabel, QMessageBox


class GaussianDialog (QDialog):
    """
    This class creates a dialog window.
    Also handles the input for the creation of the frames.
    """

    def __init__(self):
        """
        This method initializes the dialog.
        Handles a single parameter - the frame thickness.
        """
        super().__init__()
        self.setWindowTitle("Input data")

        self.layout = QFormLayout()

        info_label = QLabel("Enter an integer less than 100 for the thickness of the frame.")
        self.layout.addWidget(info_label)

        self.param1 = QLineEdit()
        number_validator_1 = QIntValidator()
        number_validator_1.setRange(1, 100)
        self.param1.setValidator(number_validator_1)

        self.layout.addRow("Frame thickness", self.param1)

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.check_input)

        self.layout.addRow(self.ok_button)

        self.setLayout(self.layout)

    def check_input(self):
        """
        Checks if the input is valid.
        :return:
        """
        input_text = self.param1.text()
        if not input_text.isdigit():
            self.show_error_message("Please enter a valid integer.")
            return

        frame_thickness = int(input_text)
        if frame_thickness > 100 :
            self.show_error_message("Please enter an integer less than 100.")
            return

        # if all is good, close the dialogue window
        self.accept()

    def show_error_message(self, message: str):
        """
        If an error occurs, shows a message box.
        :param message:
        :return:
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
