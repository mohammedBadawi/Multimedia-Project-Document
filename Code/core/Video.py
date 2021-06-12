import videokf as vf
import cv2
import glob
import numpy as np


class Video:

    def __init__(self, folder_path, videopath, methods):
        self.videopath = videopath
        self.methods = methods
        self.folder_path = folder_path

    def keyframeEX(self):
        vf.extract_keyframes(self.videopath, method=self.methods)

    def getimage(self):
        im_data = []
        im_paths = []
        files = glob.glob(self.folder_path + "\keyframes\*.jpg")
        for myFile in files:
            im_paths.append(myFile)
            image = cv2.imread(myFile)
            im_data.append(image)

        print('image shape:', np.array(im_data).shape)
        return im_paths, im_data


# using of video class
folder_path = r"D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Vid1"
video_path = r"D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Vid1\\SampleVideo_360x240_10mb.mp4"
v = Video(folder_path, video_path, "iframes")
v.keyframeEX()
print(v.getimage())
# the key frame save in the folder of the video
# videopath="video.mp4"
# vf.extract_keyframes(videopath, method="flow")
