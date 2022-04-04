"""

@authors	joseito.junior@brphotonics.com
@date   	09/03/2022

"""

from copy import copy
import logging

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit
from datetime import datetime


class Console(logging.Handler):

    def __init__(self, widget: QTextEdit, name='console'):
        super().__init__()
        self.widget = widget
        self.name = name
        self.widget.setReadOnly(True)
        self.widget.setStyleSheet(
            "background-color: rgba(0,0,0,0); border: 0px;")
        self.widget.textChanged.connect(self.widget.ensureCursorVisible)

    def clear(self):
        self.widget.clear()

    def add_logging(self, level: int = logging.INFO):
        formatter = logging.Formatter(
            '<span style="color: #999999;">%(asctime)s</span> %(message)s',
            datefmt='%H:%M:%S'
        )
        self.setFormatter(formatter)
        logging.getLogger().addHandler(self)
        logging.getLogger().setLevel(level)

    def __call__(self, *args, **kwds):
        for arg in args:
            if isinstance(arg, Msg):
                msg = arg.fmt

            elif isinstance(arg, str):
                msg = str(arg)

            else:
                continue

            for line in msg.split('<br>'):
                now = datetime.now().strftime('%H:%M:%S')
                formmated = f'<span style="color: #ff5555;">{now}</span> {line}'
                self.widget.append(formmated)

            QtCore.QCoreApplication.processEvents()

    def emit(self, record):
        if isinstance(record.msg, Msg):
            record.msg = record.msg.fmt

        for line in record.msg.split('<br>'):
            _record = copy(record)
            _record.msg = line

            msg = self.format(_record)
            self.widget.append(msg)

        QtCore.QCoreApplication.processEvents()


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
