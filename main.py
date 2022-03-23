"""

@authors	joseito.junior@brphotonics.com
@date   	10/02/2022

"""

import builtins
import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow

from qt_material import apply_stylesheet

import src.aa_update as aa_update
from resources.ui_files.main import Ui_MainWindow
from src.console import Msg, Style, create_console
from src.data import data
from src.logger import logger_print, print_exception_locals


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    print_exception_locals()


if __name__ == '__main__':
    builtins.print = logger_print
    sys.excepthook = excepthook
    root = QApplication([])
    app = Window()

    apply_stylesheet(app,
                     theme='light_blue.xml',
                     invert_secondary=True)
    app.show()
    sys.exit(root.exec_())
