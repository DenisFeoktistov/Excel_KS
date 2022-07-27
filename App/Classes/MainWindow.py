from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore


import App.App as App
import App.Classes.Action as Action


"❌"
"✔"


class Color:
    main2 = "rgb(211, 211, 211)"
    main1 = "rgb(231, 231, 231)"


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

        # self.file_scroll_area = FileScrollArea(self)
        # self.info_scroll_area = InfoScrollArea(self)

        # self.info_label = QLabel(self, text="")
        # self.info_scroll_area.add_widget(self.info_label)

        self.file_select_button = QPushButton(self)
        self.file_select_label = QLabel(self)

        self.output_file_select_button = QPushButton(self)
        self.output_file_select_label = QLabel(self)

        self.enter_button = QPushButton(self)

        self.labels = list()
        self.set_up()

    def set_up_relations(self) -> None:
        self.action = self.app.action

    def set_up(self) -> None:
        self.set_up_window()

        # self.set_up_file_scroll_area()
        # self.set_up_info_scroll_area()

        self.set_up_file_select_button()
        self.set_up_file_select_label()

        self.set_up_output_file_select_button()
        self.set_up_output_file_select_label()
        self.set_up_enter_button()

    def set_up_window(self) -> None:
        user_screen_geometry = self.app.desktop().screenGeometry()

        self.setFixedSize(self.width, self.height)
        self.move(int(user_screen_geometry.width() * (1 - MainWindow.REL_WIDTH) / 2),
                  int(user_screen_geometry.height() * (1 - MainWindow.REL_HEIGHT) / 2))

        self.setWindowTitle('Подсчет по КС')
        self.setStyleSheet('background: rgb(170, 170, 170)')

    def set_up_file_select_button(self):
        self.file_select_button.setText("Выберите файлы, которые\n необходимо обработать")

        rel_width = 0.79
        rel_height = 0.32
        self.file_select_button.setFixedSize(330, 70)
        self.file_select_button.move(5, 5)

        self.file_select_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 20px; 
                font-weight: 200; 
                background: {Color.main1};
            }}
            QPushButton:hover {{
                background: {Color.main2};
            }}
            """
        )

    def set_up_output_file_select_button(self):
        self.output_file_select_button.setText("Выберите папку, в которую\n необходимо загрузить результат")

        self.output_file_select_button.setFixedSize(330, 70)
        self.output_file_select_button.move(5, 100)

        self.output_file_select_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 20px; 
                font-weight: 200; 
                background: {Color.main1};
            }}
            QPushButton:hover {{
                background: {Color.main2};
            }}
            """
        )

    def set_up_enter_button(self):
        self.enter_button.setText("Обработать")

        self.enter_button.setFixedSize(200, 80)
        self.enter_button.move(125, 200)

        self.enter_button.setStyleSheet(
            f"""
            QPushButton {{
                border: 2px solid black; 
                border-radius: 5px; 
                font-size: 20px; 
                font-weight: 200; 
                background: {Color.main1};
            }}
            QPushButton:hover {{
                background: {Color.main2};
            }}
            """
        )

    def set_up_file_select_label(self):
        self.file_select_label.setText("❌")

        self.file_select_label.setFixedSize(70, 70)
        self.file_select_label.move(370, 5)

        self.file_select_label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 30px; font-weight: 200; background: {Color.main1}; color: red;")
        self.file_select_label.setAlignment(QtCore.Qt.AlignCenter)

    def set_up_output_file_select_label(self):
        self.output_file_select_label.setText("✔")

        self.output_file_select_label.setFixedSize(70, 70)
        self.output_file_select_label.move(370, 100)

        self.output_file_select_label.setStyleSheet(
            f"border: 1px solid black; border-radius: 5px; font-size: 30px; font-weight: 200; background: {Color.main1}; color: green;")
        self.output_file_select_label.setAlignment(QtCore.Qt.AlignCenter)

