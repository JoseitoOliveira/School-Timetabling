"""

@authors	joseito.junior@brphotonics.com
@date   	10/02/2022

"""

import builtins
from functools import partial
import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget
from PyQt5.QtCore import Qt
from qt_material import apply_stylesheet
from tinydb import Query, where

import src.aa_update
from resources.ui_files.main import Ui_MainWindow
from src.data import db, disciplinas, distancias, professores, salas
from src.logger import logger_print, print_exception_locals
from src.horarios import horarios_str, horarios_2, horarios_3
from src.console import Console
from src.modelos import Disciplina


theme_extra = {

    # Button colors
    'primaryColor': '#606060',
    'primaryLightColor': '#909090',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',

    # Font
    'font_family': 'Roboto',
}


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.console = Console(self.ui.console)
        self.console.add_logging()
        print('olá mundo')

        self.tab_discilina()
        self.tab_professores()
        self.tab_salas()

        self.ui.tab_telas.currentChanged.connect(self.change_tab)

        self.ui.list_professores.currentTextChanged.connect(
            self.professor_clicado)
        self.ui.list_salas.currentTextChanged.connect(self.sala_clicada)
        self.ui.list_disciplinas.currentTextChanged.connect(
            self.disciplina_clicada)

        self.ui.list_horarios_todos.itemDoubleClicked.connect(
            self.list_horarios_todos_item_clicked)

        self.ui.list_laboratorios.itemDoubleClicked.connect(
            self.list_laboratorios_item_clicked)

        self.ui.list_laboratorios_disciplinas.itemDoubleClicked.connect(
            partial(self.remove_item_list,
                    self.ui.list_laboratorios_disciplinas))

        self.ui.list_laboratorios_disciplinas.itemDoubleClicked.connect(
            self.atualizar_laboratorios)

        self.ui.btn_add_disciplina.clicked.connect(self.add_disciplina)
        self.ui.btn_rmv_disciplina.clicked.connect(self.rmv_disciplina)

        self.ui.nome_disciplina.textEdited.connect(
            self.nome_disciplina_changed)

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

    def grades_changed(self, grades):
        disciplina = self.disciplina_atual()
        disciplina['grades'] = grades.split()
        disciplinas.update(disciplina,
                           where('nome') == disciplina['nome'])

    def num_alunos_changed(self, value):
        disciplina = self.disciplina_atual()
        disciplina['num_alunos'] = value
        disciplinas.update(disciplina,
                           where('nome') == disciplina['nome'])

    def nome_disciplina_atual(self):
        return self.ui.list_disciplinas.currentItem().text()

    def sem_sala_changed(self, value):
        disciplina = self.disciplina_atual()
        disciplina['sem_sala'] = value
        disciplinas.update(disciplina,
                           where('nome') == disciplina['nome'])

    def sem_professor_changed(self, value):
        disciplina = self.disciplina_atual()
        disciplina['sem_professor'] = value
        disciplinas.update(disciplina,
                           where('nome') == disciplina['nome'])

    def disciplina_atual(self):
        nome = self.nome_disciplina_atual()
        disciplina = disciplinas.search(where('nome') == nome)  # type: ignore
        return disciplina[0]

    def add_aula(self):
        creditos_horarios = {
            1: horarios_str,
            2: horarios_2,
            3: horarios_3
        }
        disciplina = self.disciplina_atual()
        creditos = self.ui.num_credidos_aula.value()
        disciplina['horas'].append(creditos)
        disciplina['horarios'].append(creditos_horarios[creditos])
        disciplinas.update(disciplina,
                           where('nome') == disciplina['nome'])

        self.disciplina_clicada(self.nome_disciplina_atual())

    def rmv_aula(self):
        disciplina = self.disciplina_atual()
        aula_atual = self.ui.tab_horarios.currentIndex()
        disciplina['horas'].remove(disciplina['horas'][aula_atual])
        disciplina['horarios'].remove(disciplina['horarios'][aula_atual])
        disciplinas.update(disciplina, where('nome') == disciplina['nome'])

        self.disciplina_clicada(self.nome_disciplina_atual())

    def nome_disciplina_changed(self, nome):

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

        disciplina = self.disciplina_atual()
        nome_atual = disciplina['nome']
        disciplina['nome'] = nome
        disciplinas.update(disciplina,
                           where('nome') == nome_atual)  # type: ignore

        self.ui.list_disciplinas.currentItem().setText(nome)

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

    def list_laboratorios_item_clicked(self, item):
        self.ui.list_laboratorios_disciplinas.addItem(item.text())
        self.atualizar_laboratorios()

    def list_horarios_todos_item_clicked(self, item):
        current_tab = self.ui.tab_horarios.currentIndex()
        current_list = self.ui.tab_horarios.widget(current_tab)
        items = [
            current_list.item(i).text()
            for i in range(current_list.count())
        ] + [item.text()]
        items = list(set(items))
        items.sort()
        current_list.clear()
        current_list.addItems(items)

        disciplina = self.nome_disciplina_atual()
        self.atualizar_horarios(disciplina, current_tab)

    def remove_item_list(self, list_widget, item):
        list_widget.takeItem(list_widget.row(item))

    def professor_clicado(self, nome):
        if nome == '':
            return
        professor = professores.search(where('nome') == nome)
        self.ui.nome_professor.setText(professor[0]['nome'])
        self.ui.horas_min_professor.setValue(professor[0]['hrs_min'])
        self.ui.horas_max_professor.setValue(professor[0]['hrs_max'])

    def sala_clicada(self, nome):
        if nome == '':
            return
        sala = salas.search(where('nome') == nome)
        self.ui.nome_sala.setText(sala[0]['nome'])
        self.ui.capacidade_sala.setValue(sala[0]['capacidade'])

    def disciplina_clicada(self, nome):
        if nome == '':
            return
        disciplina = self.disciplina_atual()
        horas = [str(h) for h in disciplina['horas']]
        self.ui.nome_disciplina.setText(disciplina['nome'])
        self.ui.num_alunos.setValue(disciplina['num_alunos'])
        self.ui.grades_disciplinas.setText(" ".join(disciplina['grades']))
        self.ui.disciplina_sem_professor.setChecked(
            disciplina['sem_professor'])
        self.ui.disciplina_sem_sala.setChecked(disciplina['sem_sala'])

        while self.ui.tab_horarios.count():
            self.ui.tab_horarios.removeTab(0)

        for i, hora in enumerate(horas):
            new_tab = QListWidget()
            new_tab.itemDoubleClicked.connect(
                partial(self.remove_item_list, new_tab)
            )
            new_tab.itemDoubleClicked.connect(
                partial(self.atualizar_horarios, nome, i)
            )
            new_tab.setViewMode(QListWidget.IconMode)
            new_tab.addItems(disciplina['horarios'][i])
            self.ui.tab_horarios.addTab(new_tab, hora)

        self.ui.list_laboratorios_disciplinas.clear()
        self.ui.list_laboratorios_disciplinas.addItems(
            [lab['nome'] for lab in disciplina['laboratorios']]
        )

    def atualizar_horarios(self, nome_disciplina, indice_horarios):
        disciplina = disciplinas.search(where('nome') == nome_disciplina)[0]
        tab_horarios = self.ui.tab_horarios.currentWidget()
        horarios = [
            tab_horarios.item(i).text()
            for i in range(tab_horarios.count())
        ]
        disciplina['horarios'][indice_horarios] = horarios
        disciplinas.update(disciplina, where('nome') == nome_disciplina)

    def atualizar_laboratorios(self):
        disciplina = self.disciplina_atual()
        nomes_labs = [
            self.ui.list_laboratorios_disciplinas.item(i).text()
            for i in range(self.ui.list_laboratorios_disciplinas.count())
        ]
        disciplina['laboratorios'] = [
            salas.search(where('nome') == nome)[0]  # type: ignore
            for nome in nomes_labs
        ]
        disciplinas.update(disciplina, where('nome') == disciplina['nome'])

    def tab_discilina(self):
        self.carregar_discplinas()
        self.carregar_laboratorios()
        self.ui.list_horarios_todos.addItems(horarios_str)

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
                     theme='light_blue.xml',
                     invert_secondary=True,
                     extra=theme_extra)
    app.show()
    sys.exit(root.exec_())
