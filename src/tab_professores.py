
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QHeaderView, QTableWidgetItem)
from tinydb import where

from resources.ui_files.main import Ui_MainWindow
from src.data import disciplinas, professores, salas  # noqa
from src.horarios import horarios_str as horarios_1_str
from src.modelos import Professor  # noqa


class TabProfessores:

    def __init__(self, ui: Ui_MainWindow) -> None:

        self.ui = ui

        self.ui.list_professores.currentRowChanged.connect(
            self.set_professor_atual)

        self.ui.list_professores.currentRowChanged.connect(
            self.exibir_professor_atual)

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

        self.ui.btn_add_professor.clicked.connect(self.add_professor)
        self.ui.btn_rmv_professor.clicked.connect(self.rmv_professor)

    def nome_professor_edited(self, nome):

        nomes = [p['nome'] for p in professores.all()]
        if nome in nomes:
            self.ui.nome_professor.setStyleSheet(
                'QLineEdit { border-color:  red }'
            )
            return
        else:
            self.ui.nome_professor.setStyleSheet('')

        self.professor_atual.nome = nome
        self.ui.list_professores.currentItem().setText(nome)

    def set_professor_atual(self, *args, **kwargs):
        current_item = self.ui.list_professores.currentItem()
        if current_item is None:
            return
        professor = professores.get(where('nome') == current_item.text())
        self.professor_atual = Professor.from_json(professor)

    def exibir_professor_atual(self):
        self.ui.nome_professor.setText(self.professor_atual.nome)
        self.ui.horas_min_professor.setValue(self.professor_atual.hrs_min)
        self.ui.horas_max_professor.setValue(self.professor_atual.hrs_max)
        self.carregar_afinidade_professor_disciplina()
        self.carregar_afinidade_professor_salas()
        self.carregar_afinidade_professor_horarios()

    def atualizar(self):
        self.carregar_professores()

    def professor_afinidade_disciplina_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_disciplina.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        disciplina = self.ui.professor_afinidade_disciplina.item(
            item.row(), 0).text()
        self.professor_atual.set_afinidade_disciplinas(disciplina, afinidade)

    def professor_afinidade_horario_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_horario.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        horario = self.ui.professor_afinidade_horario.item(
            item.row(), 0).text()

        self.professor_atual.set_afinidade_horarios(horario, afinidade)

    def horas_min_professor_changed(self, value):
        self.professor_atual.hrs_min = value

    def horas_max_professor_changed(self, value):
        self.professor_atual.hrs_max = value

    def add_professor(self):
        novo_professor = Professor(nome='Novo professor')
        professores.insert(novo_professor.as_json())
        self.ui.list_professores.insertItem(0, novo_professor.nome)
        self.ui.list_professores.setCurrentRow(0)

    def rmv_professor(self):
        nome = self.professor_atual.nome
        professores.remove(where('nome') == nome)  # type: ignore
        self.ui.list_professores.takeItem(
            self.ui.list_professores.currentRow())

    def professor_afinidade_sala_changed(self, item: QTableWidgetItem):
        current_item = self.ui.professor_afinidade_sala.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        sala = self.ui.professor_afinidade_sala.item(item.row(), 0).text()
        self.professor_atual.set_afinidade_salas(sala, afinidade)

    def carregar_professores(self):
        self.ui.list_professores.clear()
        for professor in sorted(professores.all(), key=lambda x: x['nome']):
            self.ui.list_professores.addItem(professor['nome'])

    def carregar_afinidade_professor_disciplina(self):
        disciplinas_nomes = [disciplina['nome']
                             for disciplina in disciplinas.all()]

        self.ui.professor_afinidade_disciplina.setRowCount(0)

        for i, disciplina in enumerate(disciplinas_nomes):
            self.ui.professor_afinidade_disciplina.insertRow(i)
            afinidade = self.professor_atual.afinidade_disciplinas.get(
                disciplina, 0)
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
        afinidade_salas = self.professor_atual.afinidade_salas
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

        afinidade_horarios = self.professor_atual.afinidade_horarios

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
