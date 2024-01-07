# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from ui.ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.file_select_button.clicked.connect(self.open_file_dialog)

    """
    Slot function called when file_select_button is clicked sets the path to the folder containing 
    """
    def open_file_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", "/home/dheemanth")
        self.ui.folder_select_path.setText(folder_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.setWindowTitle("Library Loader")
    widget.show()
    # print(widget.size())
    sys.exit(app.exec())
