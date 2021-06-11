import random
from core.DataBase import DataBase
import cv2
import os.path
import numpy as np

from core.Techniques import Techniques

data_base = DataBase()
#
# #  VIDEO INSERT
# video_path = "D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\Shakal.mp4"
#
# inserted_video_id = data_base.insert_media(video_path, "v")
# print(inserted_video_id)
#
# #  VIDEO_KEY_FRAMES_INSERT
#
# paths_array = ["keyFrame1path", "keyFrame2path", "keyFrame3path", "keyFrame4path"]
# key_frames_histograms = [[10.0, 15.0, 60.0, 5.0, 5.0], [15.0, 20.0, 20.0, 30.0, 70.0], [15.0, 20.0, 50.0, 60.0, 5.0],
#                          [20.0, 20.0, 20.0, 10.0, 50.0]]
#
# data_base.insert_all_key_frames(inserted_video_id, paths_array, key_frames_histograms)

#  VIDEO KEY FRAMES READING WITH FILTERING


#  VIDEO KEY FRAMES INSERTING

#  histogram_input = [10.0, 15.0, 60.0, 5.0, 5.0]

histogram_input = [0.270637 , 0.128657, 0.097357, 0.229466, 0.270637]
histogram2 = [20.0, 30.0, 5.0, 50.0, 40.0]
histogram3 = [10.0, 15.0, 50.0, 10.0, 15.0]
#
mean = 13

#data_base.insert_media("path0" + ".png", "i", mean, histogram2)
#data_base.insert_media("path1" + ".png", "i", mean, histogram3)

#
# # data_base.insert_media("path0" + ".png", "i", mean, histogram2)
# # data_base.insert_media("path1" + ".png", "i", mean, histogram3)
#
#  filtered = data_base.load_images_with_filtering(histogram_input, "histogram", 0.3)

filtered = data_base.load_images_with_filtering(histogram_input, "histogram", 0.1)
for row in filtered:
    print(row[0])


img = cv2.imread("C:\\Users\\mkhef\\Desktop\\se7s.png")
print(Techniques.imageHistogram(img,(img.shape[0] * img.shape[1] * img.shape[2])))
#
#
# # filtered = data_base.load_video_key_frames_with_filtering(1, 13, 0, 5000)
# # for row in filtered:
# #     print(row)"""
#
#
# """"""
# """media_id, status = data_base.insert_media("D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\ImagesForProject"
#                                           "\\watermelon.jpg", "i")"""
#
# """print(media_id)
# result = data_base.load_all_videos()
# for row in result:
#     print(row)"""
#
# # #  main #  key frames loading
# #
#
#
# video_path = "D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\Elza3ama.mp4"
# data_base.insert_all_key_frames(1, video_path)
#
#
#
#
#
# # i = 0
# # # file = "D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\"+str(i)+".jpg"
# # while os.path.isfile(file):
# #     data_base.insert_video_key_frames(1, file)
# #     i = i+1
# #     file = "D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\"+str(i)+".jpg"
# #
# # """
# # # end
# #
# # """result = data_base.load_video_key_frames(1)
# # for row in result:
# #     print(row)"""
# #
# # #  main #  delete key frames
# # #  data_base.delete_video_key_frames(1)
# #
# #
# #
# # """watermelon = cv2.imread("D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\ImagesForProject\\watermelon.jpg")
# # cv2.imwrite("D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\watermelon.jpg", watermelon)"""
# #
# # """video_path = "D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\Elza3ama.mp4"
# #
# # cap = cv2.VideoCapture(video_path)
# # # Read the first frame.
# # success, prev_frame = cap.read()
# # i = 0
# # while success:
# #
# #     path = str(i) + ".jpg"
# #     success, curr_frame = cap.read()
# #     if curr_frame is not None:
# #         cv2.imwrite("D:\\4thComputer\\2ndTerm\\MultiMedia\\Project\\VideosForProject\\Video1\\" + path, curr_frame)
# #
# #     i = i + 1"""
