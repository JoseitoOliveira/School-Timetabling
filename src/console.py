"""

@authors	joseito.junior@brphotonics.com
@date   	09/03/2022

"""

import logging

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMainWindow, QLayout


class Console(logging.Handler):

    def __init__(self, parent):
        super().__init__()
        self.widget = QTextEdit(parent)
        self.widget.setReadOnly(True)
        self.widget.setStyleSheet(
            "background-color: rgba(0,0,0,0); border: 0px;")
        self.widget.textChanged.connect(self.widget.ensureCursorVisible)

    def clear(self):
        self.widget.clear()

    def emit(self, record):
        if isinstance(record.msg, Msg):
            record.msg = record.msg.fmt

        msg = self.format(record)
        self.widget.append(msg)
        QtCore.QCoreApplication.processEvents()


def create_console(parent: QMainWindow, container_layout: QLayout):
    logTextBox = Console(parent)
    formatter = logging.Formatter(
        '<span style="color: #ff5555;">%(asctime)s</span> %(message)s',
        datefmt='%H:%M:%S'
    )
    logTextBox.setFormatter(formatter)
    logging.getLogger().addHandler(logTextBox)
    logging.getLogger().setLevel(logging.DEBUG)

    container_layout.addWidget(logTextBox.widget)
    parent.setLayout(container_layout)


class Style:

    def __init__(self, msg, color=None, font_weight=None, font_style=None, size=None):
        self.msg = msg

        style = f'color: {color};' if color else ''
        style += f'font-weight: {font_weight};' if font_weight else ''
        style += f'font-style: {font_style};' if font_style else ''
        style += f'font-size: {size}px;' if size else ''
        self.fmt = f'<span style="{style}">{msg}</span>' if style else msg

    def __str__(self):
        return self.msg

    def __repr__(self) -> str:
        return self.msg


class Msg:

    def __init__(self, *args) -> None:
        for arg in args:
            assert isinstance(arg, str) or isinstance(arg, Style)

        self.args = args

    @property
    def fmt(self) -> str:
        msg = ''
        for arg in self.args:
            if isinstance(arg, Style):
                msg += arg.fmt.replace('\n', '<br>')
            else:
                msg += arg.replace('\n', '<br>')
        return msg

    def __str__(self) -> str:
        msg = ''
        for arg in self.args:
            if isinstance(arg, Style):
                msg += arg.msg
            else:
                msg += arg

        return msg

    def __repr__(self) -> str:
        return ''.join(self.args)
