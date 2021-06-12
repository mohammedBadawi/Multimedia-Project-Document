from PySide2.QtWidgets import QFileDialog
from GUI.mainWindow import MainWindow
from core.Core import MMCore


class MainWindowController:
    def __init__(self, gui: MainWindow):
        self.__gui = gui
        self.__start_communication()
        self.__core = MMCore()

    def __start_communication(self):
        self.__gui.browse_btn.clicked.connect(lambda: self.__on_browse_btn_clicked())
        self.__gui.insert_btn.clicked.connect(lambda: self.__on_insert_btn_clicked())
        self.__gui.search_btn.clicked.connect(lambda: self.__on_search_btn_clicked())

    def __on_browse_btn_clicked(self):
        fname = QFileDialog.getOpenFileName(self.__gui, 'Open file', 'c:\\', "Image files (*.jpg *.png *.mp4 *.avi)")[0]
        if fname != "":
            self.__gui.img_path_txt.setText(fname)
            self.__gui.img_widget.set_path(fname, load_video=True)

    def __on_insert_btn_clicked(self):
        self.__core.insert_image(self.__gui.img_path_txt.text())

    def __on_search_btn_clicked(self):
        selected_tech = self.__gui.search_by_cmbx.currentText()
        paths = []
        if selected_tech == "Mean Color":
            paths = self.__core.get_matched_images(path=self.__gui.img_path_txt.text(),
                                                   threshold=0.2,
                                                   mean=1)
            for i in len(paths[0]):
                path = paths[i]
                print("Mean" + path[0])
                self.__gui.images[i].set_path(path[0])

        elif selected_tech == "Histogram":
            paths = self.__core.get_matched_images(path=self.__gui.img_path_txt.text(),
                                                   threshold=0.4,
                                                   histogram=1)
            print("De7k")
            for i in len(paths[0]):
                path = paths[i]
                print("Histogram" + path[0])
                self.__gui.images[i].set_path(path[0])

        elif selected_tech == "Color Layout":
            paths = self.__core.get_matched_images(path=self.__gui.img_path_txt.text(),
                                                   threshold=0.7,
                                                   colorLayout=1)

            for i in len(paths[0]):
                path = paths[i]
                print("color Layout" + path[0])
                self.__gui.images[i].set_path(path[0])

        # for path in paths:
        #     i = 0
        #     self.__gui.images[i].setImagePath(path)
        #     i = i + 1


