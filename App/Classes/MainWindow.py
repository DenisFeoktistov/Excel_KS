from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton


import App.App as App
import App.Classes.Action as Action


class MainWindow(QMainWindow):
    def __init__(self, app: App.App) -> None:
        super().__init__()

        self.app = app
        self.action: Action.Action = None

        self.set_up()

    def set_up_relations(self) -> None:
        self.action = self.app.action

    def set_up(self):
        self.setFixedSize(100, 100)
        self.btn = QPushButton(parent=self, text="Click me")
        self.btn.move(10, 10)
        self.btn.setFixedSize(50, 50)

