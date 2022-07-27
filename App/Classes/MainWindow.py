from __future__ import annotations
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore


import App.App as App
import App.Classes.Action as Action


FILE_SELECT_TEXT = ""


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
        self.height = 250  # int(user_screen_geometry.height() * MainWindow.REL_HEIGHT)

        # self.file_scroll_area = FileScrollArea(self)
        # self.info_scroll_area = InfoScrollArea(self)

        # self.info_label = QLabel(self, text="")
        # self.info_scroll_area.add_widget(self.info_label)

        self.file_select_button = QPushButton(self)
        self.output_file_select_button = QPushButton(self)
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
        self.set_up_output_file_select_button()
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
        self.file_select_button.setFixedSize(int(self.width * rel_width), int(self.height * rel_height))
        self.file_select_button.move(int(self.width * 0.01), int(self.height * 0.01))

        self.file_select_button.setStyleSheet(
            "border: 2px solid black; border-radius: 5px; font-size: 20px; font-weight: 200; background: rgb(235, 71, 0); color: black;")

    def set_up_output_file_select_button(self):
        self.output_file_select_button.setText("Выберите папку, в которую\n необходимо загрузить результат")

        rel_width = 0.79
        rel_height = 0.32
        self.output_file_select_button.setFixedSize(int(self.width * rel_width), int(self.height * rel_height))
        self.output_file_select_button.move(int(self.width * 0.01), int(self.height * 0.34))

        self.output_file_select_button.setStyleSheet(
            "border: 2px solid black; border-radius: 5px; font-size: 20px; font-weight: 200; background: rgb(235, 71, 0); color: black;")

    def set_up_enter_button(self):
        self.enter_button.setText("Обработать")

        rel_width = 0.5
        rel_height = 0.30
        self.enter_button.setFixedSize(int(self.width * rel_width), int(self.height * rel_height))
        self.enter_button.move(int(self.width / 2 - self.width * rel_width / 2), int(self.height * 0.67))

        self.enter_button.setStyleSheet(
            "border: 2px solid black; border-radius: 5px; font-size: 20px; font-weight: 200; background: rgb(235, 71, 0); color: black;")

    # def set_up_file_scroll_area(self):
    #     rel_width = 0.98
    #     rel_height = 0.48
    #
    #     self.file_scroll_area.setFixedSize(int(self.width * rel_width), int(self.height * rel_height))
    #     self.file_scroll_area.move(int(self.width * 0.01), int(self.height * 0.01))
    #     self.file_scroll_area.setWidgetResizable(True)
    #
    #     self.file_scroll_area.setStyleSheet("border: 2px solid black; border-radius: 5px")
    #     self.file_scroll_area.verticalScrollBar().setStyleSheet("""
    #                                     QScrollBar {
    #                                         background: rgb(170, 170, 170);
    #                                         border: 0px solid black;
    #                                     }
    #
    #                                     QScrollBar::add-line {
    #                                         background: red;
    #                                     }
    #
    #                                     QScrollBar::sub-line:vertical {
    #                                         background: red;
    #                                     }
    #
    #                                     QScrollBar::handle {
    #                                         background: rgb(235, 71, 0);
    #                                         border: 2px solid rgb(70, 70, 70);
    #                                         border-radius: 3px;
    #                                     }
    #                                     """)
    #     self.file_scroll_area.verticalScrollBar().setFixedWidth(15)
    #     self.file_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    #
    #     self.file_scroll_area.setViewportMargins(int(self.width * 0.01), 0, int(self.width * 0.01), 0)
    #
    #     for i in range(30):
    #         self.labels.append(QLabel(parent=self, text="2 ТП-3083 ЗРЭС.xlsx"))
    #         self.file_scroll_area.add_widget(self.labels[-1])

    # def set_up_info_scroll_area(self):
    #     rel_width = 0.48
    #     rel_height = 0.98
    #
    #     self.info_scroll_area.setFixedSize(int(self.width * rel_width), int(self.height * rel_height))
    #     self.info_scroll_area.move(int(self.width * 0.01), int(self.height * 0.01))
    #     self.info_scroll_area.setWidgetResizable(True)
    #
    #     self.info_scroll_area.setStyleSheet("border: 2px solid black; border-radius: 5px")
    #     self.info_scroll_area.verticalScrollBar().setStyleSheet("""
    #                                             QScrollBar {
    #                                                 background: rgb(170, 170, 170);
    #                                                 border: 0px solid black;
    #                                             }
    #
    #                                             QScrollBar::add-line {
    #                                                 background: red;
    #                                             }
    #
    #                                             QScrollBar::sub-line:vertical {
    #                                                 background: red;
    #                                             }
    #
    #                                             QScrollBar::handle {
    #                                                 background: rgb(235, 71, 0);
    #                                                 border: 2px solid rgb(70, 70, 70);
    #                                                 border-radius: 3px;
    #                                             }
    #                                             """)
    #     self.info_scroll_area.verticalScrollBar().setFixedWidth(int(self.width * 0.02))
    #     self.info_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    #
    #     self.info_scroll_area.setViewportMargins(int(self.width * 0.01), 0, int(self.width * 0.01), 0)


# class ScrollAreaMain(QScrollArea):
#     def __init__(self, parent: QMainWindow) -> None:
#         super().__init__(parent=parent)
#         self.container = Container()
#         self.setWidget(self.container)
#
#     def add_widget(self, widget: QWidget) -> None:
#         self.container.add_widget(widget)
#
#     def clear(self) -> None:
#         self.container.clear()


# class FileScrollArea(ScrollAreaMain):
#     def set_up_widget(self, widget: QLabel) -> None:
#         widget.setFixedHeight(30)
#         widget.setFixedWidth(int((self.width() - self.verticalScrollBar().width()) * 0.93))
#         widget.setStyleSheet(
#             "border: 1px solid black; border-radius: 5px; font-size: 18px; font-weight: 300; background: rgb(51, 204, 51); color: black;")
#         widget.setAlignment(QtCore.Qt.AlignCenter)
#
#     def add_widget(self, widget: QLabel) -> None:
#         super(FileScrollArea, self).add_widget(widget)
#         self.set_up_widget(widget)



# class InfoScrollArea(ScrollAreaMain):
#     def set_up_widget(self, widget: QWidget) -> None:
#         widget.setFixedHeight(22)
#         widget.setFixedWidth(int(self.width() * 0.75))
#         widget.setStyleSheet(
#             "border: 1px solid black; border-radius: 5px; font-size: 13px; font-weight: 300; background: rgb(51, 204, 51); color: black;")
#
#     def add_widget(self, widget: QWidget) -> None:
#         super(InfoScrollArea, self).add_widget(widget)
#         self.set_up_widget(widget)


# class Container(QWidget):
#     def __init__(self) -> None:
#         super().__init__()
#         self.setLayout(QVBoxLayout())
#
#     def add_widget(self, widget: QWidget) -> None:
#         widget.setParent(self)
#         self.layout().addWidget(widget)
#
#     def clear(self) -> None:
#         for i in reversed(range(self.layout().count())):
#             self.layout().itemAt(i).widget().setParent(None)
