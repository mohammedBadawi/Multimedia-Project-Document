import numpy as np

class Techniques:

    @staticmethod
    def accurateHistogram(image):
        return np.histogram(image.ravel(),256,[0,256])[0] / (image.shape[0] * image.shape[1] * image.shape[2])

    @staticmethod
    def imageHistogram(image, numOfPixels):
        histogram = np.zeros(5)
        histValues = np.histogram(image.ravel(),256,[0,256])[0]
        valuesPerRegion = int(len(histValues)/5)
        for i in range(5):
            start = i*valuesPerRegion
            end = i*valuesPerRegion+valuesPerRegion-1
            histogram[i] = np.sum(histValues[start:end])
        histogram = histogram/numOfPixels
        return histogram

    @staticmethod
    def videoHistogram(keyFrames):
        numOfKeyFrames = len(keyFrames)
        videoHistogram = np.zeros((numOfKeyFrames,256))
        for i in range(numOfKeyFrames):
            videoHistogram[i] = Techniques.accurateHistogram(keyFrames[i])
        return videoHistogram

    @staticmethod
    def colorLayout(image): #The output is np.array of (25(columns*rows),256(the 256 values of histogram))
        layoutHistogram = np.zeros((5, 5, 256))
        valuesPerRegion = int(image.shape[0]/5) * int(image.shape[1]/5) * image.shape[2]
        row = int(image.shape[0]/5)
        column = int(image.shape[1]/5)
        for i in range(5):
            rowStart = i*row
            rowEnd = i*row + row - 1
            for j in range(5):
                columnStart = j*column
                columnEnd = j*column + column-1
                layoutHistogram[i,j] = Techniques.accurateHistogram(image[rowStart:rowEnd,columnStart:columnEnd])
        return layoutHistogram.reshape(25,256)

    @staticmethod
    def meanColor(image):
        avg_color_per_row = np.average(image, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0) #avg of each channel
        meanColor = np.average(avg_color, axis=0) #avg between the 3 channels
        return meanColor