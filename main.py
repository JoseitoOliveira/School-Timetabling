"""

@authors	joseito.junior@brphotonics.com
@date   	10/02/2022

"""

import builtins
import subprocess
import sys
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QMainWindow
from qt_material import apply_stylesheet

import src.aa_update  # noqa
from resources.ui_files.main import Ui_MainWindow
from src.logger import logger_print, print_exception_locals
from src.tab_disciplinas import TabDisciplinas
from src.tab_salas import TabSalas
from src.tab_professores import TabProfessores

theme_extra = {
    'primaryColor': '#2bcc71',
    'primaryLightColor': '#ff616f',
    'secondaryColor': '#2e415c',
    'secondaryLightColor': '#465c7a',
    'secondaryDarkColor': '#1e2c40',
    'primaryTextColor': '#000000',
    'secondaryTextColor': '#ffffff',
    # Font
    'font_family': 'Consolas',
    'density_scale': '0'
}


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() |
                            Qt.CustomizeWindowHint |
                            Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHint |
                            Qt.WindowCloseButtonHint)

        self.init_tab_executar()

        self.tab_discilinas = TabDisciplinas(self.ui)
        self.tab_professores = TabProfessores(self.ui)
        self.tab_salas = TabSalas(self.ui)

        self.ui.actionExecute.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(0))
        self.ui.actionDisciplinas.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(1))
        self.ui.actionProfessores.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(2))
        self.ui.actionSalas.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(3))
        self.ui.actionSobre.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(4))

        self.ui.tab_telas.currentChanged.connect(self.change_tab)

    def init_tab_executar(self):
        self.ui.btn_executar.clicked.connect(self.executar)

    def executar(self):
        command = (
            'start python otimizador.py '
            f'--tam_pop {self.ui.tam_pop.value()} '
            f'--num_ger {self.ui.num_ger.value()} '
            f'--taxa_cruzamento {self.ui.taxa_cruz.value()} '
            f'--taxa_mutacao {self.ui.taxa_mut.value()} '
            f'--num_repeticoes {self.ui.num_rep.value()} '
            f'--tournsize {self.ui.tournsize.value()}'
        )
        subprocess.Popen(command, shell=True)
        print(command)

    def change_tab(self, index):
        tab_functions = {
            1: self.tab_discilinas.atualizar,
            2: self.tab_professores.atualizar,
            3: self.tab_salas.atualizar
        }
        if index in tab_functions.keys():
            tab_functions[index]()


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
                     extra=theme_extra,
                     theme='dark_teal.xml')

    app.show()
    sys.exit(root.exec_())
