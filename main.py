"""

@authors	joseito.junior@brphotonics.com
@date   	10/02/2022

"""

import builtins
import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow

from qt_material import apply_stylesheet

# import src.aa_update as aa_update
from resources.ui_files.main import Ui_MainWindow
from src.console import Msg, Style, create_console
from src.data import data
from src.logger import logger_print, print_exception_locals

theme_extra = {

    # Button colors
    'primaryColor': '#213f98',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',

    'density_scale': '-1',
    # Font
    'font_family': 'Roboto',
}


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        create_console(self, self.ui.console_layout)

        self.load_types()
        self.ui.device_index.setValue(data['device_index'])

        print(Msg(
            'Olá, \n',
            Style('cor! \n', color='#00ff00'),
            Style('tamanho! \n', size=16),
            Style('espessura! \n', font_weight=800),
            Style('estilo! \n', font_style='italic'))
        )

        self.ui.btn_connect.clicked.connect(
            self.connect
        )

    def connect(self):
        print('connect')

    def load_types(self):
        self.ui.comboBox_type.clear()
        self.ui.comboBox_type.addItems(data['types'])


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
                     invert_secondary=True,
                     extra=theme_extra)
    app.showMaximized()
    sys.exit(root.exec_())
