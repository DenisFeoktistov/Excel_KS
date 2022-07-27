from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow


import App.App as App
import App.Classes.Action as Action


class MainWindow(QMainWindow):
    def __init__(self, app: App.App) -> None:
        super().__init__()

        self.app = app
        self.action: Action.Action = None

    def set_up_relations(self) -> None:
        self.action = self.app.action
