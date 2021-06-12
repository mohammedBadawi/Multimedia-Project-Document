from core.Comparator import Comparator
# from core.DataBase import DataBase
from core.DataBase import DataBase
from core.Techniques import Techniques
from core.Image import Image


# from core.Video import Video


class Integration:
    def __init__(self, videoThreshold):
        self.image = Image()
        self.comparator = Comparator(videoThreshold)
        self.data_base = DataBase()

    def getMatchedImages(self, path, threshold, mean=0, histogram=0, colorLayout=0):
        # get filtered image from data base
        filteredImages, filteredImagesPaths = self.image.getSimilarImages(self.data_base, path, mean=mean,
                                                                          appHistogram=histogram,
                                                                          colorLayout=colorLayout)

        # return filtered images as it is filtered by data base
        if mean == 1:
            return filteredImagesPaths
        # use comparator methods to get the error of every image relative to search images by using histogram
        elif histogram == 1:
            self.comparator.add_search_hist(self.image.imageAccHistogram)
        # use comparator methods to get the error of every image relative to search images by using colorLayout
        elif colorLayout == 1:
            self.comparator.add_layout_hists(self.image.imageColorLayout)

        matchedImagesPaths = []
        for i in range(len(filteredImages)):
            # calculate error using histogram technique
            if histogram == 1:
                error = self.comparator.compare_hist(Techniques().accurateHistogram(filteredImages[i]))
            # calculate error using colorLayout technique
            elif colorLayout == 1:
                error = self.comparator.compare_layout_hists(Techniques().colorLayout(filteredImages[i]))
            # compare error with threshold
            if error <= threshold:
                matchedImagesPaths.append(filteredImagesPaths[i])

        return matchedImagesPaths
