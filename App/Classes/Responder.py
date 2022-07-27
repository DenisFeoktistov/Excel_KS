from __future__ import annotations


import App.App as App
import App.Classes.MainWindow as MainWindow


class Responder:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.main_window: MainWindow.MainWindow = None

    def set_up_relations(self) -> None:
        self.main_window = self.app.main_window
