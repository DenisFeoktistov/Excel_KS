from __future__ import annotations


import App.App as App
import App.Classes.Domain as Domain
import App.Classes.MainWindow as MainWindow


class Action:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.domain = Domain.Domain()
        self.main_window: MainWindow.MainWindow = None

    def set_up_relations(self) -> None:
        self.main_window = self.app.main_window

    def select_files(self, files) -> None:
        result = self.domain.update_files(files)

        if result:
            self.main_window.tick(self.main_window.file_select_label)
        else:
            self.main_window.cross(self.main_window.file_select_label)

    def select_output_folder(self, folder):
        result = self.domain.update_output_folder(folder)

        if result:
            self.main_window.tick(self.main_window.output_file_select_label)
        else:
            self.main_window.cross(self.main_window.output_file_select_label)

    def process(self):
        self.domain.process()
