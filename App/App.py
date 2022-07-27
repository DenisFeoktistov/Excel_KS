from __future__ import annotations
from typing import Any
from PyQt5.QtWidgets import QApplication


from App.Classes.Action import Action
from App.Classes.Responder import Responder
from App.Classes.MainWindow import MainWindow


class App(QApplication):
    def __init__(self, args: Any) -> None:
        super().__init__(args)

        self.main_window = MainWindow(self)

        self.action = Action(self)
        self.responder = Responder(self)

        self.set_up_relations()

    def set_up_relations(self) -> None:
        self.action.set_up_relations()
        self.responder.set_up_relations()

    def start(self) -> None:
        self.main_window.show()
