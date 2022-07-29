from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog, QMessageBox
from PyQt5 import QtCore


import App.App as App
import App.Classes.Action as Action


class SpecialSymbols:
    TICK = "✓"
    CROSS = "✗"


class Color:
    MAIN1 = "rgb(231, 231, 231)"
    MAIN2 = "rgb(211, 211, 211)"


class MainWindow(QMainWindow):
    REL_WIDTH, REL_HEIGHT = 0.3, 0.3

    def __init__(self, app: App.App) -> None:
        super().__init__()

        self.app = app
        self.action: Action.Action = None

        # --------------------------------------------------------------------------------------------------------------
        # Graphical part

        user_screen_geometry = self.app.desktop().screenGeometry()
        self.width = 450  # int(user_screen_geometry.width() * MainWindow.REL_WIDTH)
        self.height = 300  # int(user_screen_geometry.height() * MainWindow.REL_HEIGHT)

        self.select_files_button = QPushButton(self)
        self.select_files_label = QLabel(self)

        self.select_output_folder_button = QPushButton(self)
        self.select_output_folder_label = QLabel(self)

        self.process_button = QPushButton(self)

        self.error_message = QMessageBox(self)

        self.set_up()

    def connect(self):
        self.select_files_button.clicked.connect(self.select_files)
        self.select_output_folder_button.clicked.connect(self.select_output_folder)
        self.process_button.clicked.connect(self.action.process)

    def set_up_relations(self) -> None:
        self.action = self.app.action

        self.connect()

    def set_up(self) -> None:
        self.set_up_window()

        self.set_up_select_files_button()
        self.set_up_select_files_label()

        self.set_up_select_output_folder_button()
        self.set_up_select_output_folder_label()
        self.set_up_process_button()

        self.set_up_error_message()

    def set_up_window(self) -> None:
        user_screen_geometry = self.app.desktop().screenGeometry()

        self.setFixedSize(self.width, self.height)
        self.move(int(user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2),
                  int(user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2))

        self.setWindowTitle('Подсчет по КС')
        self.setStyleSheet('background: rgb(170, 170, 170);')

    def set_up_select_files_button(self) -> None:
        self.select_files_button.setText("Выберите файлы, которые\n необходимо обработать")

        rel_width = 0.79
        rel_height = 0.32
        self.select_files_button.setFixedSize(330, 70)
        self.select_files_button.move(5, 5)

        self.select_files_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 20px; 
                font-weight: 200; 
                background: {Color.MAIN1};
            }}
            QPushButton:hover {{
                background: {Color.MAIN2};
            }}
            """
        )

    def set_up_select_output_folder_button(self) -> None:
        self.select_output_folder_button.setText("Выберите папку, в которую\n будет загружен результат")

        self.select_output_folder_button.setFixedSize(330, 70)
        self.select_output_folder_button.move(5, 100)

        self.select_output_folder_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 20px; 
                font-weight: 200; 
                background: {Color.MAIN1};
            }}
            QPushButton:hover {{
                background: {Color.MAIN2};
            }}
            """
        )

    def set_up_process_button(self) -> None:
        self.process_button.setText("Обработать")

        self.process_button.setFixedSize(200, 80)
        self.process_button.move(125, 200)

        self.process_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 25px; 
                font-weight: 200; 
                background: {Color.MAIN1};
            }}
            QPushButton:hover {{
                background: {Color.MAIN2};
            }}
            """
        )

    def set_up_select_files_label(self) -> None:
        self.select_files_label.setText(SpecialSymbols.CROSS)

        self.select_files_label.setFixedSize(50, 50)
        self.select_files_label.move(380, 15)

        self.select_files_label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 40px; font-weight: 200; background: {Color.MAIN1}; color: red;")
        self.select_files_label.setAlignment(QtCore.Qt.AlignCenter)

    def set_up_select_output_folder_label(self) -> None:
        self.select_output_folder_label.setText(SpecialSymbols.CROSS)

        self.select_output_folder_label.setFixedSize(50, 50)
        self.select_output_folder_label.move(380, 110)

        self.select_output_folder_label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 40px; font-weight: 200; background: {Color.MAIN1}; color: red;")
        self.select_output_folder_label.setAlignment(QtCore.Qt.AlignCenter)

    def set_up_error_message(self) -> None:
        self.error_message.setWindowTitle("Сообщение")
        self.error_message.setStyleSheet(f'border: 0px solid black; border-radius: 2px; font-size: 18px; font-weight: 400; background: {Color.MAIN1};')

    def select_files(self) -> None:
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "Excel files (*.xlsx)", options=options)

        self.action.select_files(files)

    def select_output_folder(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.action.select_output_folder(folder)

    def tick(self, label: QLabel) -> None:
        label.setText(SpecialSymbols.TICK)

        label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 40px; font-weight: 200; background: {Color.MAIN1}; color: green;")

    def cross(self, label: QLabel) -> None:
        label.setText(SpecialSymbols.CROSS)

        label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 40px; font-weight: 200; background: {Color.MAIN1}; color: red;")

    def show_error_message(self, text: str) -> None:
        self.error_message.setText(text)
        self.error_message.show()
