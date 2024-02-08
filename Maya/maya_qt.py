"""
This script file is for QT first assignment:

1 Create a Button that gets the selected object and prints its name [5 points] Testing Understanding of
Maya Qt
This button should be in its own window
Can be docked into the Maya UI


Note: I could solve only one assignment of QT
"""


import maya.cmds as cmds
from PySide6 import QtWidgets, QtCore


class SelectedObjectWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SelectedObjectWindow, self).__init__()
        self.setWindowTitle("Object Name")
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumWidth(200)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.selected_object_label = QtWidgets.QLabel("Selected Object:")
        self.selected_object_name = QtWidgets.QLabel("")
        self.get_object_button = QtWidgets.QPushButton("Get Selected Object")

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.selected_object_label)
        main_layout.addWidget(self.selected_object_name)
        main_layout.addWidget(self.get_object_button)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def create_connections(self):
        self.get_object_button.clicked.connect(self.get_selected_object_name)

    def get_selected_object_name(self):
        selected_objects = cmds.ls(selection=True)
        if selected_objects:
            selected_object = selected_objects[0]
            self.selected_object_name.setText(selected_object)
        else:
            self.selected_object_name.setText("No object selected")


def show_selected_object_window():
    global selected_object_window
    try:
        selected_object_window.close()
    except:
        pass
    selected_object_window = SelectedObjectWindow()
    selected_object_window.show()


# Call the function to show the window
show_selected_object_window()
