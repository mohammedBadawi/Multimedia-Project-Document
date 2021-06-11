# import cv2
class Comparator:
    def __init__(self, hist_err_th=0.3):
        self.hist_err_th = hist_err_th
        self.searh_hist = []
        self.layout_hists = []

    def add_search_hist(self, searh_hist):
        self.searh_hist = searh_hist

    def add_layout_hists(self, layout_hists):
        self.layout_hists = layout_hists

    def compare_hist(self, img_hist):
        similarity = 0

        for i in range(len(self.searh_hist)):
            similarity += min(self.searh_hist[i], img_hist[i])
        return (1 - (similarity / (sum(img_hist))))  # [0]

    def compare_layout_hists(self, img_layout_hists):
        total_err = 0
        for i in range(len(self.layout_hists)):
            similarity = 0
            for j in range(len(self.layout_hists[i])):
                similarity += min(self.layout_hists[i][j], img_layout_hists[i][j])
            total_err += 1 - (similarity / sum(img_layout_hists[i]))
        return total_err / len(self.layout_hists)

    def compare_video_key_frames_hist(self, key_frames_hist1, key_frames_hist2):
        no_of_similar_key_frames = 0
        for key_frame_hist1 in key_frames_hist1:
            self.add_search_hist(key_frame_hist1)
            for key_frame_hist2 in key_frames_hist2:
                if self.compare_hist(key_frame_hist2) < self.hist_err_th:
                    no_of_similar_key_frames += 1
                    break
        return 1 - (no_of_similar_key_frames / min([len(key_frames_hist1), len(key_frames_hist2)]))
# # unit testing
# c = Comparator()
# img1 = cv2.imread('Cameraman.png')
# norm_hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
# img2 = cv2.imread('cameraman2.png')
# hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
# norm_hist2 = hist2 * ( sum(norm_hist1) / sum(hist2) )
#
# c.add_search_hist(norm_hist1)
# print(f"histogram error ={c.compare_hist(norm_hist2)}")
#
# c.add_layout_hists([norm_hist1,norm_hist2,norm_hist1])
# print(f"layout error ={c.compare_layout_hists([norm_hist2,norm_hist2,norm_hist2])}")
#
# print(f"video error ={c.compare_video_key_frames_hist([norm_hist1,norm_hist2],[norm_hist2,norm_hist2])}")
