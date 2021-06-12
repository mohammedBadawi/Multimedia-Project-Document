from PySide2.QtCore import Qt
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout,\
    QLineEdit, QPushButton, QGroupBox, QLabel, QComboBox, QSplitter
from GUI.MediaViewer import MediaWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.img_path_txt = QLineEdit(self)
        self.browse_btn = QPushButton(self, text="Browse")
        self.insert_btn = QPushButton(self, text="Insert")
        self.clear_btn = QPushButton(self, text="Clear")
        self.search_by_cmbx = QComboBox(self)
        self.search_btn = QPushButton(self, text="Search")
        self.img_widget = QImageLabel(img_path="", parent=self)
        self.__draw()
        self.search_by_cmbx.addItems(["Mean Color", "Histogram", "Color Layout"])
        self.images = [
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
            MediaWidget(path=""),
        ]

    def __draw(self):
        mainW = QSplitter(Qt.Horizontal, parent=self)
        mainW.setLayout(QHBoxLayout())
        mainW.layout().addWidget(self.__draw_left_panel(mainW))
        mainW.layout().addWidget(self.__draw_right_panel(mainW))
        self.setCentralWidget(mainW)

    def __draw_right_panel(self, parent=None):
        rightW = QWidget(parent)
        rightW.setLayout(QGridLayout())
        # rightW.layout().addWidget(self.images[0])
        # rightW.layout().addWidget(self.images[1])
        # rightW.layout().addWidget(self.images[2])
        # rightW.layout().addWidget(self.images[3])
        # rightW.layout().addWidget(self.images[4])
        # rightW.layout().addWidget(self.images[5])
        # rightW.layout().addWidget(self.images[6])
        # rightW.layout().addWidget(self.images[7])
        # rightW.layout().addWidget(self.images[8])

        return rightW

    def __draw_left_panel(self, parent=None):
        leftW = QWidget(parent)
        lw1 = QWidget(leftW)
        lw2 = QGroupBox(leftW)
        lw3 = QWidget(leftW)

        leftW.setLayout(QVBoxLayout())
        lw1.setLayout(QGridLayout())
        lw2.setLayout(QVBoxLayout())
        lw3.setLayout(QGridLayout())

        leftW.layout().addWidget(lw1)
        leftW.layout().addWidget(lw2)
        leftW.layout().addWidget(lw3)

        lw1.layout().addWidget(QLabel("Image Path"), 0, 0, 1, 1)
        lw1.layout().addWidget(self.img_path_txt, 0, 1, 1, 6)
        lw1.layout().addWidget(self.browse_btn, 0, 7, 1, 1)
        lw1.layout().addWidget(self.insert_btn, 0, 8, 1, 1)
        lw1.layout().addWidget(self.clear_btn, 0, 9, 1, 1)

        lw2.setTitle("Selected Image")
        lw2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lw2.layout().addWidget(self.img_widget)
        self.img_widget.setScaledContents(True)

        lw3.layout().addWidget(QLabel("Search By"), 0, 0, 1, 1)
        lw3.layout().addWidget(self.search_by_cmbx, 0, 1, 1, 10)
        lw3.layout().addWidget(self.search_btn, 0, 16, 1, 1)
        return leftW