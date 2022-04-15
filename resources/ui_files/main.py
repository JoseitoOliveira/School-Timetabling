# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui_files\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 845)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(99999, 99999))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/Icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(9999, 9999))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_telas = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_telas.setElideMode(QtCore.Qt.ElideMiddle)
        self.tab_telas.setDocumentMode(True)
        self.tab_telas.setObjectName("tab_telas")
        self.tab_exec = QtWidgets.QWidget()
        self.tab_exec.setObjectName("tab_exec")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_exec)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_17 = QtWidgets.QLabel(self.tab_exec)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.tam_pop = QtWidgets.QSpinBox(self.tab_exec)
        self.tam_pop.setMaximum(99999)
        self.tam_pop.setProperty("value", 1024)
        self.tam_pop.setObjectName("tam_pop")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tam_pop)
        self.label_18 = QtWidgets.QLabel(self.tab_exec)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.num_ger = QtWidgets.QSpinBox(self.tab_exec)
        self.num_ger.setMaximum(99999)
        self.num_ger.setProperty("value", 500)
        self.num_ger.setObjectName("num_ger")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_ger)
        self.label_19 = QtWidgets.QLabel(self.tab_exec)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.num_rep = QtWidgets.QSpinBox(self.tab_exec)
        self.num_rep.setMinimum(1)
        self.num_rep.setObjectName("num_rep")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.num_rep)
        self.label_20 = QtWidgets.QLabel(self.tab_exec)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.taxa_mut = QtWidgets.QDoubleSpinBox(self.tab_exec)
        self.taxa_mut.setMaximum(0.99)
        self.taxa_mut.setSingleStep(0.01)
        self.taxa_mut.setProperty("value", 0.2)
        self.taxa_mut.setObjectName("taxa_mut")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taxa_mut)
        self.label_21 = QtWidgets.QLabel(self.tab_exec)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.taxa_cruz = QtWidgets.QDoubleSpinBox(self.tab_exec)
        self.taxa_cruz.setMaximum(0.99)
        self.taxa_cruz.setSingleStep(0.01)
        self.taxa_cruz.setProperty("value", 0.8)
        self.taxa_cruz.setObjectName("taxa_cruz")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.taxa_cruz)
        self.label_22 = QtWidgets.QLabel(self.tab_exec)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.tournsize = QtWidgets.QSpinBox(self.tab_exec)
        self.tournsize.setMinimum(1)
        self.tournsize.setMaximum(10)
        self.tournsize.setProperty("value", 3)
        self.tournsize.setObjectName("tournsize")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tournsize)
        self.btn_executar = QtWidgets.QPushButton(self.tab_exec)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/circled_play_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_executar.setIcon(icon1)
        self.btn_executar.setIconSize(QtCore.QSize(24, 24))
        self.btn_executar.setFlat(True)
        self.btn_executar.setObjectName("btn_executar")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_executar)
        self.horizontalLayout_12.addLayout(self.formLayout_4)
        self.tab_telas.addTab(self.tab_exec, "")
        self.tab_disc = QtWidgets.QWidget()
        self.tab_disc.setEnabled(True)
        self.tab_disc.setObjectName("tab_disc")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_disc)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.form_disciplina = QtWidgets.QGroupBox(self.tab_disc)
        self.form_disciplina.setEnabled(True)
        self.form_disciplina.setStyleSheet("QGroupBox{border: 0px;}")
        self.form_disciplina.setObjectName("form_disciplina")
        self.layout = QtWidgets.QFormLayout(self.form_disciplina)
        self.layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.label = QtWidgets.QLabel(self.form_disciplina)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nome_disciplina = QtWidgets.QLineEdit(self.form_disciplina)
        self.nome_disciplina.setObjectName("nome_disciplina")
        self.layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_disciplina)
        self.label_3 = QtWidgets.QLabel(self.form_disciplina)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.num_alunos = QtWidgets.QSpinBox(self.form_disciplina)
        self.num_alunos.setObjectName("num_alunos")
        self.layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.num_alunos)
        self.label_4 = QtWidgets.QLabel(self.form_disciplina)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.grades_disciplinas = QtWidgets.QLineEdit(self.form_disciplina)
        self.grades_disciplinas.setObjectName("grades_disciplinas")
        self.layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.grades_disciplinas)
        self.label_8 = QtWidgets.QLabel(self.form_disciplina)
        self.label_8.setObjectName("label_8")
        self.layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.form_disciplina)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.num_credidos_aula = QtWidgets.QSpinBox(self.form_disciplina)
        self.num_credidos_aula.setMinimum(1)
        self.num_credidos_aula.setMaximum(3)
        self.num_credidos_aula.setObjectName("num_credidos_aula")
        self.horizontalLayout_13.addWidget(self.num_credidos_aula)
        self.btn_add_aula = QtWidgets.QPushButton(self.form_disciplina)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/add_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_aula.setIcon(icon2)
        self.btn_add_aula.setIconSize(QtCore.QSize(24, 24))
        self.btn_add_aula.setFlat(True)
        self.btn_add_aula.setObjectName("btn_add_aula")
        self.horizontalLayout_13.addWidget(self.btn_add_aula)
        self.btn_rmv_aula = QtWidgets.QPushButton(self.form_disciplina)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/cancel_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rmv_aula.setIcon(icon3)
        self.btn_rmv_aula.setIconSize(QtCore.QSize(24, 24))
        self.btn_rmv_aula.setFlat(True)
        self.btn_rmv_aula.setObjectName("btn_rmv_aula")
        self.horizontalLayout_13.addWidget(self.btn_rmv_aula)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_horarios = QtWidgets.QTabWidget(self.form_disciplina)
        self.tab_horarios.setObjectName("tab_horarios")
        self.horizontalLayout.addWidget(self.tab_horarios)
        self.list_horarios_todos = QtWidgets.QListWidget(self.form_disciplina)
        self.list_horarios_todos.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.list_horarios_todos.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.list_horarios_todos.setViewMode(QtWidgets.QListView.IconMode)
        self.list_horarios_todos.setObjectName("list_horarios_todos")
        self.horizontalLayout.addWidget(self.list_horarios_todos)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(1, 1)
        self.layout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.form_disciplina)
        self.label_7.setObjectName("label_7")
        self.layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.disciplina_labs = QtWidgets.QTableWidget(self.form_disciplina)
        self.disciplina_labs.setObjectName("disciplina_labs")
        self.disciplina_labs.setColumnCount(1)
        self.disciplina_labs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.disciplina_labs.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_3.addWidget(self.disciplina_labs)
        self.disciplina_salas = QtWidgets.QTableWidget(self.form_disciplina)
        self.disciplina_salas.setShowGrid(False)
        self.disciplina_salas.setObjectName("disciplina_salas")
        self.disciplina_salas.setColumnCount(1)
        self.disciplina_salas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.disciplina_salas.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_3.addWidget(self.disciplina_salas)
        self.layout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.disciplina_sem_sala = QtWidgets.QCheckBox(self.form_disciplina)
        self.disciplina_sem_sala.setObjectName("disciplina_sem_sala")
        self.horizontalLayout_11.addWidget(self.disciplina_sem_sala)
        self.disciplina_sem_professor = QtWidgets.QCheckBox(self.form_disciplina)
        self.disciplina_sem_professor.setObjectName("disciplina_sem_professor")
        self.horizontalLayout_11.addWidget(self.disciplina_sem_professor)
        self.layout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.horizontalLayout_2.addWidget(self.form_disciplina)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.tab_disc)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.choques = QtWidgets.QTableWidget(self.tab_disc)
        self.choques.setShowGrid(False)
        self.choques.setGridStyle(QtCore.Qt.DashDotLine)
        self.choques.setCornerButtonEnabled(False)
        self.choques.setColumnCount(1)
        self.choques.setObjectName("choques")
        self.choques.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.choques.setHorizontalHeaderItem(0, item)
        self.verticalLayout_5.addWidget(self.choques)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.tab_disc)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.list_disciplinas = QtWidgets.QListWidget(self.tab_disc)
        self.list_disciplinas.setObjectName("list_disciplinas")
        self.verticalLayout_10.addWidget(self.list_disciplinas)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_add_disciplina = QtWidgets.QPushButton(self.tab_disc)
        self.btn_add_disciplina.setIcon(icon2)
        self.btn_add_disciplina.setIconSize(QtCore.QSize(24, 24))
        self.btn_add_disciplina.setFlat(True)
        self.btn_add_disciplina.setObjectName("btn_add_disciplina")
        self.horizontalLayout_10.addWidget(self.btn_add_disciplina)
        self.btn_rmv_disciplina = QtWidgets.QPushButton(self.tab_disc)
        self.btn_rmv_disciplina.setIcon(icon3)
        self.btn_rmv_disciplina.setIconSize(QtCore.QSize(24, 24))
        self.btn_rmv_disciplina.setFlat(True)
        self.btn_rmv_disciplina.setObjectName("btn_rmv_disciplina")
        self.horizontalLayout_10.addWidget(self.btn_rmv_disciplina)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.tab_telas.addTab(self.tab_disc, "")
        self.tab_profs = QtWidgets.QWidget()
        self.tab_profs.setObjectName("tab_profs")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_profs)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.form_professor = QtWidgets.QGroupBox(self.tab_profs)
        self.form_professor.setEnabled(True)
        self.form_professor.setStyleSheet("QGroupBox{border: 0px;}")
        self.form_professor.setObjectName("form_professor")
        self.layout_2 = QtWidgets.QFormLayout(self.form_professor)
        self.layout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_2.setObjectName("layout_2")
        self.label_9 = QtWidgets.QLabel(self.form_professor)
        self.label_9.setObjectName("label_9")
        self.layout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.nome_professor = QtWidgets.QLineEdit(self.form_professor)
        self.nome_professor.setObjectName("nome_professor")
        self.layout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_professor)
        self.label_2 = QtWidgets.QLabel(self.form_professor)
        self.label_2.setObjectName("label_2")
        self.layout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horas_min_professor = QtWidgets.QSpinBox(self.form_professor)
        self.horas_min_professor.setObjectName("horas_min_professor")
        self.layout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horas_min_professor)
        self.label_5 = QtWidgets.QLabel(self.form_professor)
        self.label_5.setObjectName("label_5")
        self.layout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horas_max_professor = QtWidgets.QSpinBox(self.form_professor)
        self.horas_max_professor.setObjectName("horas_max_professor")
        self.layout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horas_max_professor)
        self.label_12 = QtWidgets.QLabel(self.form_professor)
        self.label_12.setObjectName("label_12")
        self.layout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.professor_afinidade_disciplina = QtWidgets.QTableWidget(self.form_professor)
        self.professor_afinidade_disciplina.setRowCount(3)
        self.professor_afinidade_disciplina.setObjectName("professor_afinidade_disciplina")
        self.professor_afinidade_disciplina.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_disciplina.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_disciplina.setHorizontalHeaderItem(1, item)
        self.layout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.professor_afinidade_disciplina)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.professor_afinidade_horario = QtWidgets.QTableWidget(self.form_professor)
        self.professor_afinidade_horario.setRowCount(3)
        self.professor_afinidade_horario.setObjectName("professor_afinidade_horario")
        self.professor_afinidade_horario.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_horario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_horario.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_4.addWidget(self.professor_afinidade_horario)
        self.professor_afinidade_sala = QtWidgets.QTableWidget(self.form_professor)
        self.professor_afinidade_sala.setRowCount(3)
        self.professor_afinidade_sala.setObjectName("professor_afinidade_sala")
        self.professor_afinidade_sala.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_sala.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.professor_afinidade_sala.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_4.addWidget(self.professor_afinidade_sala)
        self.layout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5.addWidget(self.form_professor)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_professores = QtWidgets.QListWidget(self.tab_profs)
        self.list_professores.setProperty("showDropIndicator", False)
        self.list_professores.setObjectName("list_professores")
        self.verticalLayout.addWidget(self.list_professores)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_add_professor = QtWidgets.QPushButton(self.tab_profs)
        self.btn_add_professor.setIcon(icon2)
        self.btn_add_professor.setIconSize(QtCore.QSize(24, 24))
        self.btn_add_professor.setFlat(True)
        self.btn_add_professor.setObjectName("btn_add_professor")
        self.horizontalLayout_7.addWidget(self.btn_add_professor)
        self.btn_rmv_professor = QtWidgets.QPushButton(self.tab_profs)
        self.btn_rmv_professor.setIcon(icon3)
        self.btn_rmv_professor.setIconSize(QtCore.QSize(24, 24))
        self.btn_rmv_professor.setFlat(True)
        self.btn_rmv_professor.setObjectName("btn_rmv_professor")
        self.horizontalLayout_7.addWidget(self.btn_rmv_professor)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.tab_telas.addTab(self.tab_profs, "")
        self.tab_salas = QtWidgets.QWidget()
        self.tab_salas.setObjectName("tab_salas")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_salas)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.form_sala = QtWidgets.QGroupBox(self.tab_salas)
        self.form_sala.setEnabled(True)
        self.form_sala.setStyleSheet("QGroupBox{border: 0px;}")
        self.form_sala.setObjectName("form_sala")
        self.layout_3 = QtWidgets.QFormLayout(self.form_sala)
        self.layout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.layout_3.setContentsMargins(-1, 0, 0, 0)
        self.layout_3.setObjectName("layout_3")
        self.label_13 = QtWidgets.QLabel(self.form_sala)
        self.label_13.setObjectName("label_13")
        self.layout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.nome_sala = QtWidgets.QLineEdit(self.form_sala)
        self.nome_sala.setObjectName("nome_sala")
        self.layout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome_sala)
        self.label_14 = QtWidgets.QLabel(self.form_sala)
        self.label_14.setObjectName("label_14")
        self.layout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.capacidade_sala = QtWidgets.QSpinBox(self.form_sala)
        self.capacidade_sala.setObjectName("capacidade_sala")
        self.layout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.capacidade_sala)
        self.label_15 = QtWidgets.QLabel(self.form_sala)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.layout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sala_afinidade_horario = QtWidgets.QTableWidget(self.form_sala)
        self.sala_afinidade_horario.setObjectName("sala_afinidade_horario")
        self.sala_afinidade_horario.setColumnCount(2)
        self.sala_afinidade_horario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sala_afinidade_horario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sala_afinidade_horario.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_6.addWidget(self.sala_afinidade_horario)
        self.sala_distancias = QtWidgets.QTableWidget(self.form_sala)
        self.sala_distancias.setObjectName("sala_distancias")
        self.sala_distancias.setColumnCount(2)
        self.sala_distancias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sala_distancias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sala_distancias.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_6.addWidget(self.sala_distancias)
        self.layout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.eh_laboratorio = QtWidgets.QCheckBox(self.form_sala)
        self.eh_laboratorio.setObjectName("eh_laboratorio")
        self.layout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.eh_laboratorio)
        self.horizontalLayout_8.addWidget(self.form_sala)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_salas = QtWidgets.QListWidget(self.tab_salas)
        self.list_salas.setObjectName("list_salas")
        self.verticalLayout_3.addWidget(self.list_salas)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_add_sala = QtWidgets.QPushButton(self.tab_salas)
        self.btn_add_sala.setIcon(icon2)
        self.btn_add_sala.setIconSize(QtCore.QSize(24, 24))
        self.btn_add_sala.setFlat(True)
        self.btn_add_sala.setObjectName("btn_add_sala")
        self.horizontalLayout_9.addWidget(self.btn_add_sala)
        self.btn_rmv_sala = QtWidgets.QPushButton(self.tab_salas)
        self.btn_rmv_sala.setIcon(icon3)
        self.btn_rmv_sala.setIconSize(QtCore.QSize(24, 24))
        self.btn_rmv_sala.setFlat(True)
        self.btn_rmv_sala.setObjectName("btn_rmv_sala")
        self.horizontalLayout_9.addWidget(self.btn_rmv_sala)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.tab_telas.addTab(self.tab_salas, "")
        self.tab_sobre = QtWidgets.QWidget()
        self.tab_sobre.setObjectName("tab_sobre")
        self.tab_telas.addTab(self.tab_sobre, "")
        self.gridLayout.addWidget(self.tab_telas, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionExecute = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/play_button_circled_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExecute.setIcon(icon4)
        self.actionExecute.setObjectName("actionExecute")
        self.actionDisciplinas = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/books2_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisciplinas.setIcon(icon5)
        self.actionDisciplinas.setObjectName("actionDisciplinas")
        self.actionProfessores = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/team2_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProfessores.setIcon(icon6)
        self.actionProfessores.setObjectName("actionProfessores")
        self.actionSalas = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/room_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalas.setIcon(icon7)
        self.actionSalas.setObjectName("actionSalas")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources\\ui_files\\../images/info2_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSobre.setIcon(icon8)
        self.actionSobre.setObjectName("actionSobre")
        self.toolBar.addAction(self.actionExecute)
        self.toolBar.addAction(self.actionDisciplinas)
        self.toolBar.addAction(self.actionProfessores)
        self.toolBar.addAction(self.actionSalas)
        self.toolBar.addAction(self.actionSobre)

        self.retranslateUi(MainWindow)
        self.tab_telas.setCurrentIndex(0)
        self.tab_horarios.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UFPB School Timetabling"))
        self.label_17.setText(_translate("MainWindow", "Tamanho da População:"))
        self.label_18.setText(_translate("MainWindow", "Número de Gerações:"))
        self.label_19.setText(_translate("MainWindow", "Número de Repetições:"))
        self.label_20.setText(_translate("MainWindow", "Taxa de Mutação:"))
        self.label_21.setText(_translate("MainWindow", "Taxa de Cruzamento:"))
        self.label_22.setText(_translate("MainWindow", "Tamanho do Torneio:"))
        self.btn_executar.setText(_translate("MainWindow", "Iniciar"))
        self.tab_telas.setTabText(self.tab_telas.indexOf(self.tab_exec), _translate("MainWindow", "Executar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "Número de Alunos:"))
        self.label_4.setText(_translate("MainWindow", "Grades:"))
        self.label_8.setText(_translate("MainWindow", "Horários"))
        self.label_6.setText(_translate("MainWindow", "Créditos da aula:"))
        self.btn_add_aula.setText(_translate("MainWindow", "Adicionar aula"))
        self.btn_rmv_aula.setText(_translate("MainWindow", "Remover aula"))
        self.label_7.setText(_translate("MainWindow", "Laboratórios"))
        item = self.disciplina_labs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Laboratório"))
        item = self.disciplina_salas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sala"))
        self.disciplina_sem_sala.setText(_translate("MainWindow", "Sem Sala"))
        self.disciplina_sem_professor.setText(_translate("MainWindow", "Sem Professor"))
        self.label_10.setText(_translate("MainWindow", "Evitar choques com"))
        self.choques.setSortingEnabled(True)
        item = self.choques.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Disciplina"))
        self.label_11.setText(_translate("MainWindow", "Disciplinas"))
        self.btn_add_disciplina.setText(_translate("MainWindow", "Adicionar"))
        self.btn_rmv_disciplina.setText(_translate("MainWindow", "Remover"))
        self.tab_telas.setTabText(self.tab_telas.indexOf(self.tab_disc), _translate("MainWindow", "Disciplinas"))
        self.label_9.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Mínimo de Horas:"))
        self.label_5.setText(_translate("MainWindow", "Máximo de Horas:"))
        self.label_12.setText(_translate("MainWindow", "Afinidades:"))
        item = self.professor_afinidade_disciplina.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Disciplina"))
        item = self.professor_afinidade_disciplina.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afinidade"))
        item = self.professor_afinidade_horario.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.professor_afinidade_horario.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afinidade"))
        item = self.professor_afinidade_sala.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sala"))
        item = self.professor_afinidade_sala.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afinidade"))
        self.btn_add_professor.setText(_translate("MainWindow", "Adicionar"))
        self.btn_rmv_professor.setText(_translate("MainWindow", "Remover"))
        self.tab_telas.setTabText(self.tab_telas.indexOf(self.tab_profs), _translate("MainWindow", "Professores"))
        self.label_13.setText(_translate("MainWindow", "Nome:"))
        self.label_14.setText(_translate("MainWindow", "Capacidade:"))
        item = self.sala_afinidade_horario.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Horário"))
        item = self.sala_afinidade_horario.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afinidade"))
        item = self.sala_distancias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sala"))
        item = self.sala_distancias.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Distância"))
        self.eh_laboratorio.setText(_translate("MainWindow", "Laboratório"))
        self.btn_add_sala.setText(_translate("MainWindow", "Adicionar"))
        self.btn_rmv_sala.setText(_translate("MainWindow", "Remover"))
        self.tab_telas.setTabText(self.tab_telas.indexOf(self.tab_salas), _translate("MainWindow", "Salas"))
        self.tab_telas.setTabText(self.tab_telas.indexOf(self.tab_sobre), _translate("MainWindow", "Sobre"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionExecute.setText(_translate("MainWindow", "Execute"))
        self.actionDisciplinas.setText(_translate("MainWindow", "Disciplinas"))
        self.actionProfessores.setText(_translate("MainWindow", "Professores"))
        self.actionSalas.setText(_translate("MainWindow", "Salas"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
