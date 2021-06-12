import cv2
from core.Techniques import Techniques


# from core.DataBase import DataBase


class Image:
    # data_base = DataBase()

    def __init__(self, path: str):
        self.getImage(path)

    def getImageMean(self):
        return Techniques().meanColor(self.img)

    def getImageAccHist(self):
        return Techniques().accurateHistogram(self.img)

    def getImageAppHist(self):
        return Techniques().imageHistogram(self.img, self.numberofpixel)

    def getImageColorLayout(self):
        return Techniques().colorLayout(self.img)

    def getImage(self, path):
        self.img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        self.numberofpixel = self.img.shape[0] * self.img.shape[1] * self.img.shape[2]

    def imageData(self, path, colorLayout=0, accHistogram=0, appHistogram=0, mean=0):
        print(mean, appHistogram, accHistogram, colorLayout)
        self.getImage(path)
        if (mean == 1):
            self.imageMean = self.getImageMean()
        elif (appHistogram == 1):
            self.imageAppHistogram = self.getImageAppHist()
            print(self.imageAppHistogram)
        elif (accHistogram == 1):
            self.imageAccHistogram = self.getImageAccHist()
            print("Here")
        elif (colorLayout == 1):
            self.imageColorLayout = self.getImageColorLayout()

    def getSimilarImages(self, data_base, path, colorLayout=0, accHistogram=0, appHistogram=0, mean=0):  # data base
        self.imageData(path, colorLayout, accHistogram, appHistogram, mean)
        filteredImagesPaths = []
        if mean == 1:
            filteredImagesPaths = data_base.load_images_with_filtering(self.imageMean, "mean", 0.15)
            print("From Mean Color")
        elif appHistogram == 1:
            filteredImagesPaths = data_base.load_images_with_filtering(self.imageAppHistogram, "histogram", 0.49)
            print("From Histogram")
            print("Input Hist" + str(self.imageAppHistogram))
        elif colorLayout == 1:
            filteredImagesPaths = data_base.load_all_images()

        filteredImagesPaths = list(filteredImagesPaths)
        filteredImages = []
        for i in range(len(filteredImagesPaths)):
            print(filteredImagesPaths[i][0])
            filteredImages.append(cv2.imread(filteredImagesPaths[i][0], cv2.IMREAD_UNCHANGED))

        for path in filteredImagesPaths:
            print("Database " + path[0])
        return filteredImages, filteredImagesPaths
