
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QHeaderView, QListWidget,
                             QTableWidgetItem)
from tinydb import where

from resources.ui_files.main import Ui_MainWindow
from src.data import disciplinas,  salas  # noqa
from src.horarios import horarios_str as horarios_1_str
from src.modelos import Disciplina


class TabDisciplinas:

    def __init__(self, ui: Ui_MainWindow) -> None:

        self.ui = ui

        self.ui.choques.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.choques.horizontalHeader().hide()
        self.ui.choques.verticalHeader().hide()

        self.ui.disciplina_salas.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.disciplina_salas.verticalHeader().hide()

        self.ui.disciplina_labs.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.disciplina_labs.verticalHeader().hide()
        self.ui.disciplina_labs.itemChanged.connect(
            self.disciplina_labs_changed)

        self.ui.disciplina_salas.itemChanged.connect(
            self.disciplina_salas_changed)

        self.ui.choques.itemChanged.connect(self.choques_changed)

        self.ui.list_disciplinas.currentRowChanged.connect(
            self.set_disciplina_atual)

        self.ui.list_disciplinas.currentRowChanged.connect(
            self.exibir_disciplina_atual)

        self.ui.list_horarios_todos.itemDoubleClicked.connect(
            self.disciplina_add_horario)

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

    def carregar_discplinas(self):
        self.ui.list_disciplinas.clear()
        for disciplina in sorted(disciplinas.all(), key=lambda x: x['nome']):
            self.ui.list_disciplinas.addItem(disciplina['nome'])

    def atualizar(self):
        self.carregar_discplinas()
        self.ui.list_horarios_todos.clear()
        self.ui.list_horarios_todos.addItems(horarios_1_str)

    def grades_changed(self, grades):
        grades = grades.split(' ')
        if grades != self.disciplina_atual.grades:
            self.disciplina_atual.grades = grades

    def num_alunos_changed(self, value):
        if value != self.disciplina_atual.num_alunos:
            self.disciplina_atual.num_alunos = value

    def sem_sala_changed(self, value):
        if value != self.disciplina_atual.sem_sala:
            self.disciplina_atual.sem_sala = value

    def sem_professor_changed(self, value):
        if value != self.disciplina_atual.sem_professor:
            self.disciplina_atual.sem_professor = value

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

        self.disciplina_atual.nome = nome
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
        nome = self.disciplina_atual.nome
        disciplinas.remove(where('nome') == nome)  # type: ignore
        self.ui.list_disciplinas.takeItem(
            self.ui.list_disciplinas.currentRow())

    def disciplina_add_horario(self, item):
        aula = self.ui.tab_horarios.currentIndex()
        self.disciplina_atual.add_horario(aula, item.text())
        self.exibir_disciplina_atual()

    def disciplina_rmv_horario(self, item):
        aula = self.ui.tab_horarios.currentIndex()
        self.disciplina_atual.rmv_horario(aula, item.text())
        self.exibir_disciplina_atual()

    def set_disciplina_atual(self, *args, **kwargs):
        current_item = self.ui.list_disciplinas.currentItem()
        if current_item is None:
            return
        disciplina = disciplinas.get(where('nome') == current_item.text())
        self.disciplina_atual = Disciplina.from_json(disciplina)

    def exibir_disciplina_atual(self, *args, **kwargs):
        self.ui.nome_disciplina.setText(self.disciplina_atual.nome)
        self.ui.num_alunos.setValue(self.disciplina_atual.num_alunos)
        self.ui.grades_disciplinas.setText(
            " ".join(self.disciplina_atual.grades))
        self.ui.disciplina_sem_professor.setChecked(
            self.disciplina_atual.sem_professor)
        self.ui.disciplina_sem_sala.setChecked(self.disciplina_atual.sem_sala)

        self.carregar_choques_disciplina()
        self.carregar_salas_disciplina()
        self.carregar_horarios_disciplina()
        self.carregar_laboratorios_disciplina()

    def carregar_laboratorios_disciplina(self):
        self.ui.disciplina_labs.setRowCount(0)
        nomes_labs = [s.nome for s in self.disciplina_atual.laboratorios]
        labs = salas.search(where('laboratorio') == True)  # noqa
        self.ui.disciplina_labs.itemChanged.disconnect()
        for lab in sorted(labs, key=lambda d: d['nome']):
            cell = QTableWidgetItem(lab['nome'])
            cell.setFlags(Qt.ItemFlag.ItemIsEnabled |
                          Qt.ItemFlag.ItemIsUserCheckable)
            if lab['nome'] in nomes_labs:
                cell.setCheckState(Qt.CheckState.Checked)
            else:
                cell.setCheckState(Qt.CheckState.Unchecked)
            index = self.ui.disciplina_labs.rowCount()
            self.ui.disciplina_labs.insertRow(index)
            self.ui.disciplina_labs.setItem(index, 0, cell)

        self.ui.disciplina_labs.itemChanged.connect(
            self.disciplina_labs_changed)

    def carregar_horarios_disciplina(self):
        horas = [str(h) for h in self.disciplina_atual.horas]

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

    def carregar_salas_disciplina(self):
        self.ui.disciplina_salas.itemChanged.disconnect()
        self.ui.disciplina_salas.setRowCount(0)
        nomes_salas = [s.nome for s in self.disciplina_atual.salas]
        for sala in sorted(salas.all(), key=lambda d: d['nome']):
            cell = QTableWidgetItem(sala['nome'])
            cell.setFlags(Qt.ItemFlag.ItemIsEnabled |
                          Qt.ItemFlag.ItemIsUserCheckable)
            if sala['nome'] in nomes_salas:
                cell.setCheckState(Qt.CheckState.Checked)
            else:
                cell.setCheckState(Qt.CheckState.Unchecked)
            index = self.ui.disciplina_salas.rowCount()
            self.ui.disciplina_salas.insertRow(index)
            self.ui.disciplina_salas.setItem(index, 0, cell)

        self.ui.disciplina_salas.itemChanged.connect(
            self.disciplina_salas_changed
        )

    def disciplina_salas_changed(self, item):
        if item.checkState() == Qt.CheckState.Checked:
            self.disciplina_atual.add_sala(item.text())
        else:
            self.disciplina_atual.rmv_sala(item.text())

    def carregar_choques_disciplina(self):
        self.ui.choques.setRowCount(0)
        self.ui.choques.itemChanged.disconnect()
        for disciplina in sorted(disciplinas.all(), key=lambda d: d['nome']):
            if set(self.disciplina_atual.grades).intersection(
                    set(disciplina['grades'])
            ):
                continue
            cell = QTableWidgetItem(disciplina['nome'])
            cell.setFlags(Qt.ItemFlag.ItemIsEnabled |
                          Qt.ItemFlag.ItemIsUserCheckable)
            if disciplina['nome'] in self.disciplina_atual.choques:
                cell.setCheckState(Qt.CheckState.Checked)
            else:
                cell.setCheckState(Qt.CheckState.Unchecked)
            index = self.ui.choques.rowCount()
            self.ui.choques.insertRow(index)
            self.ui.choques.setItem(index, 0, cell)
        self.ui.choques.itemChanged.connect(self.choques_changed)

    def disciplina_labs_changed(self, item: QTableWidgetItem):
        if item.checkState() == Qt.CheckState.Checked:
            self.disciplina_atual.add_lab(item.text())
        else:
            self.disciplina_atual.rmv_lab(item.text())

    def choques_changed(self, item: QTableWidgetItem):
        if item.checkState() == Qt.CheckState.Checked:
            self.disciplina_atual.add_choque(item.text())
        else:
            self.disciplina_atual.rmv_choque(item.text())
