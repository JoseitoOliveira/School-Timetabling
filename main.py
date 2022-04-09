"""

@authors	joseito.junior@brphotonics.com
@date   	10/02/2022

"""

import builtins
import sys
import traceback
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHeaderView, QListWidget,
                             QMainWindow, QTableWidgetItem)
from qt_material import apply_stylesheet
from tinydb import where

import src.aa_update
from resources.ui_files.main import Ui_MainWindow
from src.console import Console
from src.data import disciplinas, distancias, professores, salas
from src.horarios import horarios_2_str, horarios_3_str
from src.horarios import horarios_str as horarios_1_str
from src.logger import logger_print, print_exception_locals
from src.modelos import Disciplina, Professor, Sala

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

        self.console = Console(self.ui.console)
        self.console.add_logging()
        print('olá mundo')

        self.init_tab_disciplinas()
        self.init_tab_professores()
        self.init_tab_salas()

        self.tab_discilina()
        self.tab_professores()
        self.tab_salas()

        self.ui.actionExecute.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(0))
        self.ui.actionDisciplinas.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(1))
        self.ui.actionProfessores.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(2))
        self.ui.actionSalas.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(3))
        self.ui.actionsobre.triggered.connect(
            lambda: self.ui.tab_telas.setCurrentIndex(4))

        self.ui.tab_telas.currentChanged.connect(self.change_tab)

    def init_tab_disciplinas(self):

        self.ui.list_disciplinas.currentRowChanged.connect(
            self.set_disciplina_atual)

        self.ui.list_disciplinas.currentRowChanged.connect(
            self.exibir_disciplina_atual)

        self.ui.list_horarios_todos.itemDoubleClicked.connect(
            self.disciplina_add_horario)

        self.ui.list_laboratorios.itemDoubleClicked.connect(
            self.disciplina_add_laboratorio)

        self.ui.list_laboratorios_disciplinas.itemDoubleClicked.connect(
            self.disciplina_rmv_laboratorio)

        self.ui.btn_add_disciplina.clicked.connect(self.add_disciplina)
        self.ui.btn_rmv_disciplina.clicked.connect(self.rmv_disciplina)
        self.ui.nome_disciplina.textEdited.connect(
            self.nome_disciplina_edited)

        self.ui.num_alunos.valueChanged.connect(
            self.num_alunos_changed)

        self.ui.grades_disciplinas.textEdited.connect(
            self.grades_changed)

        self.ui.disciplina_sem_sala.stateChanged.connect(
            self.sem_sala_changed)

        self.ui.disciplina_sem_professor.stateChanged.connect(
            self.sem_professor_changed)

        self.ui.btn_add_aula.clicked.connect(self.add_aula)
        self.ui.btn_rmv_aula.clicked.connect(self.rmv_aula)

        self.ui.list_disciplinas.setCurrentRow(0)

    def init_tab_salas(self):

        self.ui.eh_laboratorio.stateChanged.connect(
            self.eh_laboratorio_changed)

        # self.ui.btn_add_sala.clicked.connect(self.add_sala)
        # self.ui.btn_rmv_sala.clicked.connect(self.rmv_sala)

        self.ui.capacidade_sala.valueChanged.connect(
            self.capacidade_sala_changed)

        self.ui.list_salas.currentRowChanged.connect(self.sala_clicada)

        self.ui.sala_afinidade_horarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.sala_distancias.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def init_tab_professores(self):

        self.ui.list_professores.currentRowChanged.connect(
            self.professor_clicado)

        self.ui.professor_afinidade_disciplina.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.professor_afinidade_horario.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.professor_afinidade_sala.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.professor_afinidade_disciplina.itemChanged.connect(
            self.professor_afinidade_disciplina_changed
        )

        self.ui.professor_afinidade_horario.itemChanged.connect(
            self.professor_afinidade_horario_changed
        )

        self.ui.professor_afinidade_sala.itemChanged.connect(
            self.professor_afinidade_sala_changed
        )

        self.ui.nome_professor.textEdited.connect(
            self.nome_professor_edited)

        self.ui.horas_min_professor.valueChanged.connect(
            self.horas_min_professor_changed)

        self.ui.horas_max_professor.valueChanged.connect(
            self.horas_max_professor_changed)

        # self.ui.btn_add_professor.clicked.connect(self.add_professor)
        # self.ui.btn_rmv_professor.clicked.connect(self.rmv_professor)

    def capacidade_sala_changed(self, value):
        sala = self.sala_atual()
        sala['capacidade'] = value
        salas.update(sala, where('nome') == sala['nome'])

    def eh_laboratorio_changed(self, value: bool):
        sala = self.sala_atual()
        sala['laboratorio'] = value
        salas.update(sala, where('nome') == sala['nome'])

    def horas_min_professor_changed(self, value):
        professor = self.professor_atual()
        professor.set_hrs_min(value)

    def horas_max_professor_changed(self, value):
        professor = self.professor_atual()
        professor.set_hrs_max(value)

    def add_professor(self):
        ...

    def rmv_professor(self):
        ...

    def professor_afinidade_sala_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_sala.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        sala = self.ui.professor_afinidade_sala.itemAt(
            0, item.column()).text()
        professor = self.professor_atual()
        professor.set_afinidade_salas(sala, afinidade)

    def professor_afinidade_horario_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_horario.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        horario = self.ui.professor_afinidade_horario.itemAt(
            0, item.column()).text()
        professor = self.professor_atual()
        professor.set_afinidade_horarios(horario, afinidade)

    def professor_afinidade_disciplina_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_disciplina.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        disciplina = self.ui.professor_afinidade_disciplina.itemAt(
            0, item.column()).text()
        professor = self.professor_atual()
        professor.set_afinidade_disciplinas(disciplina, afinidade)

    def carregar_afinidade_professor_disciplina(self):
        professor = self.professor_atual()
        afinidade_disciplinas = professor.afinidade_disciplinas
        disciplinas_nomes = [disciplina['nome']
                             for disciplina in disciplinas.all()]

        self.ui.professor_afinidade_disciplina.setRowCount(0)

        for i, disciplina in enumerate(disciplinas_nomes):
            self.ui.professor_afinidade_disciplina.insertRow(i)
            afinidade = afinidade_disciplinas.get(disciplina, 0)
            cell_nome = QTableWidgetItem(disciplina)
            cell_nome.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_afinidade = QTableWidgetItem(str(afinidade))
            self.ui.professor_afinidade_disciplina.setItem(
                i, 0, cell_nome
            )

            self.ui.professor_afinidade_disciplina.setItem(
                i, 1, cell_afinidade
            )

    def carregar_afinidade_professor_salas(self):
        professor = self.professor_atual()
        afinidade_salas = professor.afinidade_salas
        salas_nomes = [sala['nome'] for sala in salas.all()]

        self.ui.professor_afinidade_sala.setRowCount(0)

        for i, sala in enumerate(salas_nomes):
            self.ui.professor_afinidade_sala.insertRow(i)
            afinidade = afinidade_salas.get(sala, 0)
            cell_nome = QTableWidgetItem(sala)
            cell_nome.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_afinidade = QTableWidgetItem(str(afinidade))
            self.ui.professor_afinidade_sala.setItem(
                i, 0, cell_nome
            )

            self.ui.professor_afinidade_sala.setItem(
                i, 1, cell_afinidade
            )

    def carregar_afinidade_professor_horarios(self):
        professor = self.professor_atual()
        afinidade_horarios = professor.afinidade_horarios

        self.ui.professor_afinidade_horario.setRowCount(0)

        for i, horario in enumerate(horarios_1_str):
            self.ui.professor_afinidade_horario.insertRow(i)
            afinidade = afinidade_horarios.get(horario, 0)
            cell_nome = QTableWidgetItem(horario)
            cell_nome.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_afinidade = QTableWidgetItem(str(afinidade))
            self.ui.professor_afinidade_horario.setItem(
                i, 0, cell_nome
            )

            self.ui.professor_afinidade_horario.setItem(
                i, 1, cell_afinidade
            )

    def grades_changed(self, grades):
        self.disciplina_atual.set_grades(grades)

    def num_alunos_changed(self, value):
        self.disciplina_atual.set_num_alunos(value)

    def sem_sala_changed(self, value):
        self.disciplina_atual.set_sem_sala(value)

    def sem_professor_changed(self, value):
        self.disciplina_atual.set_sem_professor(value)

    def nome_sala_atual(self):
        return self.ui.list_salas.currentItem().text()

    def sala_atual(self):
        return salas.get(where('nome') == self.nome_sala_atual())

    def nome_professor_atual(self):
        return self.ui.list_professores.currentItem().text()

    def professor_atual(self):
        nome_professor = self.nome_professor_atual()
        professor = professores.get(where('nome') == nome_professor)
        return Professor(**professor)

    def nome_disciplina_atual(self):
        return self.ui.list_disciplinas.currentItem().text()

    def add_aula(self):
        creditos = self.ui.num_credidos_aula.value()
        self.disciplina_atual.add_aula(creditos)
        self.exibir_disciplina_atual()

    def rmv_aula(self):
        aula_atual = self.ui.tab_horarios.currentIndex()
        self.disciplina_atual.rmv_aula(aula_atual)
        self.exibir_disciplina_atual()

    def nome_disciplina_edited(self, nome):

        nomes = [
            item.text()
            for item in self.ui.list_disciplinas.findItems(
                nome, Qt.MatchFlag.MatchExactly)
        ]
        if nome in nomes:
            self.ui.nome_disciplina.setStyleSheet(
                'QLineEdit { border-color:  red }'
            )
            return
        else:
            self.ui.nome_disciplina.setStyleSheet('')

        self.disciplina_atual.set_nome(nome)
        self.ui.list_disciplinas.currentItem().setText(nome)

    def nome_professor_edited(self, nome):

        nomes = [p['nome'] for p in professores.all()]
        if nome in nomes:
            self.ui.nome_professor.setStyleSheet(
                'QLineEdit { border-color:  red }'
            )
            return
        else:
            self.ui.nome_professor.setStyleSheet('')

        professor = self.professor_atual()
        professor.set_nome(nome)
        self.ui.list_professores.currentItem().setText(nome)

    def add_disciplina(self):
        nova_disciplina = Disciplina(
            nome='Nova disciplina',
            num_alunos=0,
            grades=['nova disciplina'],
            horas=[2, 2],
        )
        disciplinas.insert(nova_disciplina.as_json())
        self.ui.list_disciplinas.insertItem(0, nova_disciplina.nome)
        self.ui.list_disciplinas.setCurrentRow(0)

    def rmv_disciplina(self):
        nome = self.nome_disciplina_atual()
        disciplinas.remove(where('nome') == nome)  # type: ignore
        self.ui.list_disciplinas.takeItem(
            self.ui.list_disciplinas.currentRow())

    def disciplina_add_laboratorio(self, item):
        self.disciplina_atual.add_laboratorio(item.text())
        self.exibir_disciplina_atual()

    def disciplina_add_horario(self, item):
        aula = self.ui.tab_horarios.currentIndex()
        self.disciplina_atual.add_horario(aula, item.text())
        self.exibir_disciplina_atual()

    def disciplina_rmv_horario(self, item):
        aula = self.ui.tab_horarios.currentIndex()
        self.disciplina_atual.rmv_horario(aula, item.text())
        self.exibir_disciplina_atual()

    def remove_item_list(self, list_widget, item):
        list_widget.takeItem(list_widget.row(item))

    def carregar_afinidade_sala_horarios(self):
        sala = self.sala_atual()
        afinidade_horarios = sala['afinidade_horarios']

        self.ui.sala_afinidade_horarios.setRowCount(0)

        for i, horario in enumerate(horarios_1_str):
            self.ui.sala_afinidade_horarios.insertRow(i)
            afinidade = afinidade_horarios.get(horario, 0)
            cell_nome = QTableWidgetItem(horario)
            cell_nome.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_afinidade = QTableWidgetItem(str(afinidade))
            self.ui.sala_afinidade_horarios.setItem(
                i, 0, cell_nome
            )

            self.ui.sala_afinidade_horarios.setItem(
                i, 1, cell_afinidade
            )

    def professor_clicado(self, row):
        if row == -1:
            self.ui.form_professor.setEnabled(False)
            return
        self.ui.form_professor.setEnabled(True)
        professor = self.professor_atual()
        self.ui.nome_professor.setText(professor.nome)
        self.ui.horas_min_professor.setValue(professor.hrs_min)
        self.ui.horas_max_professor.setValue(professor.hrs_max)
        self.carregar_afinidade_professor_disciplina()
        self.carregar_afinidade_professor_salas()
        self.carregar_afinidade_professor_horarios()

    def sala_clicada(self, row):
        if row == -1:
            self.ui.form_sala.setEnabled(False)
            return
        self.ui.form_sala.setEnabled(True)
        sala = self.sala_atual()
        self.ui.nome_sala.setText(sala['nome'])
        self.ui.capacidade_sala.setValue(sala['capacidade'])
        self.ui.eh_laboratorio.setChecked(sala['laboratorio'])
        self.carregar_afinidade_sala_horarios()

    def set_disciplina_atual(self, *args, **kwargs):
        current_item = self.ui.list_disciplinas.currentItem()
        if current_item is None:
            return
        disciplina = disciplinas.get(where('nome') == current_item.text())
        self.disciplina_atual = Disciplina(**disciplina)

    def exibir_disciplina_atual(self, *args, **kwargs):
        horas = [str(h) for h in self.disciplina_atual.horas]
        self.ui.nome_disciplina.setText(self.disciplina_atual.nome)
        self.ui.num_alunos.setValue(self.disciplina_atual.num_alunos)
        self.ui.grades_disciplinas.setText(
            " ".join(self.disciplina_atual.grades))
        self.ui.disciplina_sem_professor.setChecked(
            self.disciplina_atual.sem_professor)
        self.ui.disciplina_sem_sala.setChecked(self.disciplina_atual.sem_sala)

        while self.ui.tab_horarios.count():
            self.ui.tab_horarios.removeTab(0)

        for i, hora in enumerate(horas):
            new_tab = QListWidget()
            new_tab.itemDoubleClicked.connect(
                self.disciplina_rmv_horario
            )
            new_tab.setViewMode(QListWidget.IconMode)
            new_tab.addItems(self.disciplina_atual.horarios[i])
            self.ui.tab_horarios.addTab(new_tab, hora)

        self.ui.list_laboratorios_disciplinas.clear()
        self.ui.list_laboratorios_disciplinas.addItems(
            [lab['nome'] for lab in self.disciplina_atual.laboratorios]
        )

    def disciplina_rmv_laboratorio(self, item):
        self.disciplina_atual.rmv_laboratorio(item.text())
        self.exibir_disciplina_atual()

    def tab_discilina(self):
        self.carregar_discplinas()
        self.carregar_laboratorios()
        self.ui.list_horarios_todos.addItems(horarios_1_str)

    def tab_professores(self):
        self.carregar_professores()

    def tab_salas(self):
        self.carregar_salas()

    def change_tab(self, index):
        tab_functions = {
            1: self.tab_discilina,
            2: self.tab_professores,
            3: self.tab_salas
        }
        if index in tab_functions.keys():
            tab_functions[index]()

    def carregar_laboratorios(self):
        self.ui.list_laboratorios.clear()
        labs = salas.search(where('laboratorio') == True)  # type: ignore
        self.ui.list_laboratorios.addItems([lab['nome'] for lab in labs])

    def carregar_salas(self):
        self.ui.list_salas.clear()
        for sala in salas.all():
            self.ui.list_salas.addItem(sala['nome'])

    def carregar_discplinas(self):
        self.ui.list_disciplinas.clear()
        for disciplina in sorted(disciplinas.all(), key=lambda x: x['nome']):
            self.ui.list_disciplinas.addItem(disciplina['nome'])

    def carregar_professores(self):
        self.ui.list_professores.clear()
        for professor in professores.all():
            self.ui.list_professores.addItem(professor['nome'])


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
