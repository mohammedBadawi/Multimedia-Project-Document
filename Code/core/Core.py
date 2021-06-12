import numpy as np

from core.Comparator import Comparator
from core.DataBase import DataBase
from core.Image import Image
from core.Techniques import Techniques
from core.Video import Video

class MMCore:
    def __init__(self, thershhold=0.2):
        self.__db = DataBase()
        self.__comparator = Comparator(thershhold)

    def insert_image(self, path: str):
        img = Image(path)
        self.__db.insert_media(path, "i", img.getImageMean(), img.getImageAppHist())
        print(img.getImageAppHist())

    def get_matched_images(self, path, threshold, mean=0, histogram=0, colorLayout=0):
        img = Image(path)

        filteredImages, filteredImagesPaths = img.getSimilarImages(self.__db, path, mean=mean,
                                                                   appHistogram=histogram,
                                                                   colorLayout=colorLayout)
        # return filtered images as it is filtered by data base
        if mean == 1:
            return filteredImagesPaths
        # use comparator methods to get the error of every image relative to search images by using histogram
        elif histogram == 1:
            self.__comparator.add_search_hist(img.getImageAccHist())

        # use comparator methods to get the error of every image relative to search images by using colorLayout
        elif colorLayout == 1:
            self.__comparator.add_layout_hists(img.imageColorLayout)

        matchedImagesPaths = []
        print("Hey")
        # for img in filteredImages:
        #     print(img)
        error = 5
        for i in range(len(filteredImages)):
            # calculate error using histogram technique
            if histogram == 1:
                error = self.__comparator.compare_hist(Techniques().accurateHistogram(filteredImages[i]))
                print(error)
            # calculate error using colorLayout technique
            elif colorLayout == 1:
                error = self.__comparator.compare_layout_hists(Techniques().colorLayout(filteredImages[i]))
            # compare error with threshold
            if error <= threshold:
                matchedImagesPaths.append(filteredImagesPaths[i])

        return matchedImagesPaths

        #  return filteredImagesPaths

    def getSimilarVideos(self, threshold, videoPath, folderPath):
        v = Video(folderPath, videoPath, "iframes")
        v.keyframeEX()
        inputKeyFrames = v.getimage()[1]

        dbKeyFramesPaths = GET_KEYFRAMS_FROM_DB() #array of paths 2D array every video has its key frames
        dbKeyFrames = []
        for i in len(dbKeyFramesPaths):
            dbKeyFrames.append(cv2.imread(dbKeyFramesPaths[i], cv2.IMREAD_UNCHANGED))

        inputKeyFramesHist = Techniques.videoHistogram(inputKeyFrames)
        matchedVideoPaths = []
        for i in len(dbKeyFramesPaths):
            error = self.__comparator.compare_video_key_frames_hist(inputKeyFramesHist,
                                                                    Techniques.videoHistogram(dbKeyFrames))
            if error <= threshold:
                matchedVideoPaths.append(dbKeyFramesPaths[i])

        return matchedVideoPaths


