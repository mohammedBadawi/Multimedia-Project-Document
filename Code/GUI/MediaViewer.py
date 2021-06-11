from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from GUI.QImageLabel import QImageLabel
from core.Video import Video


class MediaWidget(QWidget):
    
    def __init__(self, path="", parent=None):
        super(MediaWidget, self).__init__(parent)
        self.__next = QPushButton(text="Next Frame")
        self.__prev = QPushButton(text="Previous Frame")
        self.__path = path
        self.__path_lbl = QLabel(text="Path: " + path)
        self.__path_lbl.setWordWrap(True)
        self.__img = QImageLabel()
        self.__frames = []
        self.__f_index = 0
        self.__draw()
        self.set_path(path)
        self.__next.clicked.connect(lambda: self.__on_next_clicked())
        self.__prev.clicked.connect(lambda: self.__on_prev_clicked())

    def __draw(self):
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.__path_lbl)
        self.layout().addWidget(self.__img)
        btns_layout = QHBoxLayout()
        btns_layout.addWidget(self.__next)
        btns_layout.addWidget(self.__prev)
        self.layout().addLayout(btns_layout)
        self.__img.setScaledContents(True)

    def set_path(self, path, load_video=False, video_path=""):
        if type(path) is list:
            self.__path_lbl.setText("Path: " + video_path)
            self.__next.setVisible(True)
            self.__prev.setVisible(True)
            self.__frames = path
            self.__img.setImagePath(self.__frames[0])
            self.__f_index = 0
            return

        if path == "":
            self.__next.setVisible(False)
            self.__prev.setVisible(False)
            return

        ext = path[path.rindex('.') + 1:].upper()
        f_path = path[:path.rindex("/")]
        self.__path_lbl.setText("Path: " + path)

        if ext == "JPG" or ext == "PNG":
            self.__next.setVisible(False)
            self.__prev.setVisible(False)
            self.__img.setImagePath(path)
        else:
            self.__next.setVisible(True)
            self.__prev.setVisible(True)
            if load_video:
                v = Video(videopath=path, folder_path=f_path, methods="iframes")
                v.keyframeEX()
                self.__frames = v.getimage()[0]
                self.__img.setImagePath(self.__frames[0])
                self.__f_index = 0

    def __on_next_clicked(self):
        self.__f_index += 1
        if self.__f_index >= len(self.__frames): self.__f_index = 0
        self.__img.setImagePath(self.__frames[self.__f_index])

    def __on_prev_clicked(self):
        self.__f_index -= 1
        if self.__f_index < 0: self.__f_index = len(self.__frames) - 1
        self.__img.setImagePath(self.__frames[self.__f_index])
