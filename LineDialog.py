from PyQt5.QtGui import QIntValidator, QPixmap
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDialog, QFormLayout, QLabel, QMessageBox


class CircleDialog(QDialog):
    """
    This class creates a dialog window.
    Also handles input needed to create a line.
    """

    def __init__(self, img: tuple):
        """
        This method initializes the dialog.
        Also handles the input for the creation of the line.
        :param img:
        """
        super().__init__()
        self.setWindowTitle("Input data for a line")
        pixmap = QPixmap(img[0])
        image_size = pixmap.size()
        self.layout = QFormLayout()

        info_label = QLabel("Enter some integer data")
        self.layout.addWidget(info_label)

        self.param1 = QLineEdit()
        number_validator_1 = QIntValidator()
        number_validator_1.setRange(1, image_size.width())
        self.param1.setValidator(number_validator_1)

        self.layout.addRow("X coords of the first point", self.param1)

        self.param2 = QLineEdit()
        number_validator_2 = QIntValidator()
        number_validator_2.setRange(1, image_size.height())
        self.param2.setValidator(number_validator_2)
        self.layout.addRow("Y coords of the first point", self.param2)

        self.param3 = QLineEdit()
        number_validator_3 = QIntValidator()
        number_validator_3.setRange(1, image_size.width())
        self.param3.setValidator(number_validator_3)

        self.layout.addRow("X coords of the second point", self.param3)

        self.param4 = QLineEdit()
        number_validator_4 = QIntValidator()
        number_validator_4.setRange(1, image_size.height())
        self.param2.setValidator(number_validator_4)
        self.layout.addRow("Y coords of the second point", self.param4)

        self.param5 = QLineEdit()
        number_validator_5 = QIntValidator()
        number_validator_5.setRange(1, image_size.height() // 2)
        self.param5.setValidator(number_validator_5)

        self.layout.addRow("Enter the thickness of the line", self.param5)

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.check_input)

        self.layout.addRow(self.ok_button)

        self.setLayout(self.layout)

    def check_input(self):
        """
        Checks if the input is valid and is an integer.
        :return:
        """
        input_text_1 = self.param1.text()
        input_text_2 = self.param2.text()
        input_text_3 = self.param3.text()
        input_text_4 = self.param4.text()
        input_text_5 = self.param5.text()

        if not input_text_1.isdigit() or not input_text_2.isdigit() or not input_text_3.isdigit()\
                or not input_text_4.isdigit() or not input_text_5.isdigit():
            self.show_error_message("Please enter a valid integer.")
            return

        # if all is good close the dialog
        self.accept()

    def show_error_message(self, message: str):
        """
        Handles the error messages.
        :param message:
        :return:
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
