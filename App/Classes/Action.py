from __future__ import annotations


import App.App as App
import App.Classes.Domain as Domain
import App.Classes.MainWindow as MainWindow

from App.Classes.Domain import Messages


class Action:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.domain = Domain.Domain()
        self.main_window: MainWindow.MainWindow = None

    def set_up_relations(self) -> None:
        self.main_window = self.app.main_window

    def select_files(self, files) -> None:
        result = self.domain.update_files(files)

        if result == Messages.FILES:
            self.main_window.cross(self.main_window.select_files_label)
        else:
            self.main_window.tick(self.main_window.select_files_label)

    def select_output_folder(self, folder) -> None:
        result = self.domain.update_output_folder(folder)

        if result == Messages.FOLDER:
            self.main_window.cross(self.main_window.select_output_folder_label)
        else:
            self.main_window.tick(self.main_window.select_output_folder_label)

    def process(self) -> None:
        result = self.domain.process()

        if result != Messages.OK:
            self.main_window.show_error_message(result)
        else:
            self.main_window.show_error_message("Данные успешно обработаны")
