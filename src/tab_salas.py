
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QHeaderView, QTableWidgetItem)
from tinydb import where

from resources.ui_files.main import Ui_MainWindow
from src.data import salas  # noqa
from src.horarios import horarios_str as horarios_1_str
from src.modelos import Sala  # noqa


class TabSalas:

    def __init__(self, ui: Ui_MainWindow) -> None:
        self.ui = ui

        self.ui.eh_laboratorio.stateChanged.connect(
            self.eh_laboratorio_changed)

        self.ui.btn_add_sala.clicked.connect(self.add_sala)
        self.ui.btn_rmv_sala.clicked.connect(self.rmv_sala)

        self.ui.sala_afinidade_horario.itemChanged.connect(
            self.sala_afinidade_horario_changed
        )

        self.ui.sala_distancias.itemChanged.connect(
            self.sala_distancias_changed
        )

        self.ui.capacidade_sala.valueChanged.connect(
            self.capacidade_sala_changed)

        self.ui.list_salas.currentRowChanged.connect(self.set_sala_atual)
        self.ui.list_salas.currentRowChanged.connect(self.exibir_sala_atual)

        self.ui.sala_afinidade_horario.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.ui.sala_distancias.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    def add_sala(self):
        nova_sala = Sala(nome='Nova sala', capacidade=30)
        salas.insert(nova_sala.as_json())
        self.ui.list_salas.insertItem(0, nova_sala.nome)
        self.ui.list_salas.setCurrentRow(0)

    def rmv_sala(self):
        current_row = self.ui.list_salas.currentRow()
        if current_row == -1:
            return
        nome = self.sala_atual.nome
        salas.remove(where('nome') == nome)  # type: ignore
        self.ui.list_salas.takeItem(current_row)

    def carregar_afinidade_sala_horarios(self):
        afinidade_horarios = self.sala_atual.afinidade_horarios

        self.ui.sala_afinidade_horario.setRowCount(0)

        for i, horario in enumerate(horarios_1_str):
            self.ui.sala_afinidade_horario.insertRow(i)
            afinidade = afinidade_horarios.get(horario, 0)
            cell_nome = QTableWidgetItem(horario)
            cell_nome.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_afinidade = QTableWidgetItem(str(afinidade))
            self.ui.sala_afinidade_horario.setItem(
                i, 0, cell_nome
            )

            self.ui.sala_afinidade_horario.setItem(
                i, 1, cell_afinidade
            )

    def carregar_distancia_salas(self):
        self.ui.sala_distancias.setRowCount(0)
        distancias = self.sala_atual.distancias
        outras_salas = [
            sala['nome']
            for sala in salas.all()
            if sala['nome'] != self.sala_atual.nome
        ]

        for outra_sala in sorted(outras_salas):
            index = self.ui.sala_distancias.rowCount()
            self.ui.sala_distancias.insertRow(index)
            cell_sala = QTableWidgetItem(outra_sala)
            cell_sala.setFlags(Qt.ItemFlag.ItemIsEnabled)
            cell_dist = QTableWidgetItem(str(distancias.get(outra_sala, 1000)))
            self.ui.sala_distancias.setItem(index, 0, cell_sala)
            self.ui.sala_distancias.setItem(index, 1, cell_dist)

    def exibir_sala_atual(self):
        self.ui.nome_sala.setText(self.sala_atual.nome)
        self.ui.capacidade_sala.setValue(self.sala_atual.capacidade)
        self.ui.eh_laboratorio.setChecked(self.sala_atual.laboratorio)
        self.carregar_afinidade_sala_horarios()
        self.carregar_distancia_salas()

    def set_sala_atual(self, *args, **kwargs):
        current_item = self.ui.list_salas.currentItem()
        if current_item is None:
            return
        sala = salas.get(where('nome') == current_item.text())
        self.sala_atual = Sala.from_json(sala)

    def capacidade_sala_changed(self, value):
        self.sala_atual.capacidade = value

    def atualizar(self):
        self.carregar_salas()

    def eh_laboratorio_changed(self, value: bool):
        self.sala_atual.laboratorio = bool(value)

    def sala_afinidade_horario_changed(self, item: QTableWidgetItem):
        current_item = self.ui.sala_afinidade_horario.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            afinidade = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        horario = self.ui.sala_afinidade_horario.item(item.row(), 0).text()

        self.sala_atual.set_afinidade_horarios(horario, afinidade)

    def sala_distancias_changed(self, item: QTableWidgetItem):
        current_item = self.ui.sala_distancias.currentItem()
        if item != current_item or item.column() != 1:
            return

        try:
            distancia = int(item.text())
        except ValueError:
            print('Valor inválido')
            return

        sala = self.ui.sala_distancias.item(item.row(), 0).text()

        self.sala_atual.set_distancia(sala, distancia)

    def carregar_salas(self):
        self.ui.list_salas.clear()
        for sala in sorted(salas.all(), key=lambda x: x['nome']):
            self.ui.list_salas.addItem(sala['nome'])
