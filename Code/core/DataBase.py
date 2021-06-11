import imghdr
import os

import sqlalchemy
from sqlalchemy import MetaData, Column, Integer, String, Table, desc, func, ForeignKey, Float
from sqlalchemy.engine import ResultProxy


class DataBase:
    engine = sqlalchemy.create_engine('mysql://root:root@localhost/multimedia')  # connect to server
    conn = engine.connect()
    meta = MetaData()

    images_table = Table('images', meta,
                         Column('id', Integer, primary_key=True),
                         Column('path', String(100), primary_key=False, nullable=False, unique=True),
                         Column('mean_color', Integer, primary_key=False),
                         Column('hist1', Integer, primary_key=False),
                         Column('hist2', Float, primary_key=False),
                         Column('hist3', Float, primary_key=False),
                         Column('hist4', Float, primary_key=False),
                         Column('hist5', Float, primary_key=False)
                         )

    videos_table = Table('videos', meta,
                         Column('id', Integer, primary_key=True, unique=True, autoincrement=True),
                         Column('path', String(100), primary_key=False, nullable=False, unique=True)
                         )
    video_key_frames_table = Table('video_key_frames', meta,
                                   Column('video_id', Integer, ForeignKey(videos_table.columns['id']),
                                          primary_key=True, unique=False),
                                   Column('path', String(100), primary_key=True, nullable=False, unique=False),

                                   Column('hist1', Float, primary_key=False),
                                   Column('hist2', Float, primary_key=False),
                                   Column('hist3', Float, primary_key=False),
                                   Column('hist4', Float, primary_key=False),
                                   Column('hist5', Float, primary_key=False)
                                   )

    def insert_media(self, path, media_type, mean_color=None, histogram=None):
        if media_type == 'i':
            # media_t = imghdr.what(path)
            media_t = "png"
            #  print(media_t)
            if media_t == "jpeg" or media_t == "jpg" or media_t == "png":
                self.engine.execute("SET @count = 0;UPDATE `images` SET `images`.`id` = @count:= @count + 1; ALTER "
                                    "TABLE `images` AUTO_INCREMENT = 1; ")

                ins = self.images_table.insert().values(path=path, mean_color=mean_color,
                                                        hist1=histogram[0],
                                                        hist2=histogram[1],
                                                        hist3=histogram[2],
                                                        hist4=histogram[3],
                                                        hist5=histogram[4])
                result = self.conn.execute(ins)
                return result.inserted_primary_key[0]

            else:
                return -1

        elif media_type == 'v':
            self.engine.execute("SET @count = 0;UPDATE `videos` SET `videos`.`id` = @count:= @count + 1; ALTER "
                                "TABLE `videos` AUTO_INCREMENT = 1; ")

            ins = self.videos_table.insert().values(path=path)
            result = self.conn.execute(ins)
            return result.inserted_primary_key[0]

    def load_all_images(self):
        all_images = self.engine.execute(f'SELECT path FROM images')
        print(all_images)
        return all_images

    def formatter_data(self, res):

        assert isinstance(res, ResultProxy)
        assert res.returns_rows
        rows = []
        for _row in res.cursor._rows:
            row = {}
            for index, column in enumerate(res._metadata.keys):
                row[column] = _row[index]
            rows.append(row)
            return rows

    def load_images_with_filtering(self, feature, feature_type, threshold):  # threshold
        filtered = None
        if feature_type == "mean":  # meanColor
            filtered = self.engine.execute(
                f'SELECT path FROM images WHERE ABS(mean_color - {feature})  < {threshold}*255 ')

        elif feature_type == "histogram":  # histogram
            hist1 = feature[0]
            hist2 = feature[1]
            hist3 = feature[2]
            hist4 = feature[3]
            hist5 = feature[4]
            filtered = self.engine.execute(f'SELECT path FROM images WHERE( 1-( ( LEAST(hist1 , {hist1}) +  LEAST('
                                           f'hist2 , {hist2}) + LEAST(hist3 , {hist3}) '
                                           f'+LEAST(hist4 , {hist4}) + LEAST(hist5 , {hist5})  ) / (hist1+hist2+hist3'
                                           f'+hist4+hist5) )            )      < {threshold}')

        return filtered

    # def load_images_with_filtering(self, feature, feature_type, threshold):  # threshold
    #     filtered = None
    #     if feature_type == "mean":  # meanColor
    #         filtered = self.conn.execute(
    #             'SELECT path FROM images WHERE ABS(mean_color - {})  < {}*255 '.format(feature, feature,
    #                                                                                    threshold))
    #     elif feature_type == "histogram":  # histogram
    #         hist1 = feature[0]
    #         hist2 = feature[1]
    #         hist3 = feature[2]
    #         hist4 = feature[3]
    #         hist5 = feature[4]
    #         filtered = self.conn.execute(f'SELECT path FROM images WHERE( 1-( ( LEAST(hist1 , {hist1}) +  LEAST('
    #                                        f'hist2 , {hist2}) + LEAST(hist3 , {hist3}) '
    #                                        f'+LEAST(hist4 , {hist4}) + LEAST(hist5 , {hist5})  ) / (hist1+hist2+hist3'
    #                                        f'+hist4+hist5) )            )      < {threshold}')
    #
    #     #  print(self.formatter_data(filtered))
    #     return filtered.first()

    def load_all_key_frames(self, video_path, input_histogram, threshold):
        result_dict = {}
        video_ids, video_paths = self.load_all_videos()
        for video_id, video_path in zip(video_ids, video_paths):
            filtered_key_frames = self.load_video_key_frames_with_filtering(video_id, input_histogram, threshold)
            result_dict[video_path].append(filtered_key_frames)

        return result_dict

    def load_video_key_frames_with_filtering(self, video_id, input_histogram, threshold):  # threshold

        hist1 = input_histogram[0]
        hist2 = input_histogram[1]
        hist3 = input_histogram[2]
        hist4 = input_histogram[3]
        hist5 = input_histogram[4]
        filtered = self.engine.execute(f'SELECT path FROM video_key_frames WHERE video_id = {video_id} AND ( 1-( ( '
                                       f'LEAST(hist1 , {hist1}) + '
                                       'LEAST( '
                                       f'hist2 , {hist2}) + LEAST(hist3 , {hist3}) '
                                       f'+LEAST(hist4 , {hist4}) + LEAST(hist5 , {hist5})  ) / (hist1+hist2+hist3'
                                       f'+hist4+hist5) )            )      < {threshold}')

        return filtered

    def load_all_videos(self):
        return self.conn.execute("SELECT video_id, path FROM videos")

    def insert_all_key_frames(self, video_id, paths_array, hist_2d_array):
        if len(paths_array) == len(hist_2d_array):
            for path, histogram in zip(paths_array, hist_2d_array):
                self.insert_video_key_frames(video_id, path, histogram)
        else:
            print("Paths are not consistent in size with histograms")

    def insert_video_key_frames(self, video_id, path, histogram):
        ins = self.video_key_frames_table.insert().values(video_id=video_id, path=path,
                                                          hist1=histogram[0],
                                                          hist2=histogram[1],
                                                          hist3=histogram[2],
                                                          hist4=histogram[3],
                                                          hist5=histogram[4])
        result = self.conn.execute(ins)
        return result.inserted_primary_key[0], 1

    def load_video_key_frames(self, video_id):
        sel = self.video_key_frames_table.select(self.video_key_frames_table.columns['video_id'] == video_id).order_by(
            (func.length(self.video_key_frames_table.columns['path'])))
        return self.conn.execute(sel)

    def add_column(self, table_name, column):
        column_name = column.compile(dialect=self.engine.dialect)
        column_type = column.type.compile(self.engine.dialect)
        self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))

    def delete_video_key_frames(self, video_id):
        delete = self.video_key_frames_table.delete().where(self.video_key_frames_table.columns['video_id'] == video_id)
        self.conn.execute(delete)

    def delete_images(self):
        delete = self.images_table.delete()
        self.conn.execute(delete)
