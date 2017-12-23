import os
import datetime as dt
import random
import numpy as np

from PIL import Image
from onehot import onehot

class ImageProcessing:
    def __init__(self, save_dir_path, width=300, height=300, w_h_rate=1.35):
        """
        @param save_dir_path:保存するディレクトリ先
        """
        self.__save_dir_path = save_dir_path
        self.__mkdir()
        # 背景の大きさ
        self.__width = width
        self.__height = height
        # 牌の縦横比
        self.__w_h_rate = w_h_rate


    def __mkdir(self):
        """
        ディレクトリの存在有無を確認後、ディレクトリを作成
        """
        if not(os.path.exists(self.__save_dir_path)):
            os.mkdir(self.__save_dir_path)
            print("ディレクトリ {}を作成しました".format(self.__save_dir_path))


    def process_image(self, use_tiles, tile_dataset_path, scatter=False):
        """
        指定牌で画像を生成する
        @param use_tiles:使用する牌
            例:["m1", "s4", "haku", "n"]
        @param tile_dataset_path:使用する牌の種類(パス)
        @param scatter:牌の画像をバラバラに配置する(True)か並べるか(False)

        return:
            {作成した画像名:[教師データの情報], [], ...}
            教師データの情報
                [0:3]:次元の情報で物体を囲む矩形の位置(xmin, ymin, xmax, ymax),
                [4:37]:34クラスのonehot
                    |- m*:マンズの*[4:12]
                    |- p*:筒子の*[13:21]
                    |_- s*:ソウズの*[22:30]
                    |- (e,s,w,n):(東、南、西、北)[31:34]
                    |- haku:白[35]
                    |- hatsu:發[36]
                    |- chun:中[37]
        """
        time_ = str(dt.datetime.today()).replace(" ", "T").replace(".", ":")
        img_name = time_+".jpg"
        use_tile_quantity = len(use_tiles)
        # 座標とクラスの情報を格納するリスト
        tile_info_ = []
        # 座標等の情報と画像名を結びつける
        tile_info = {}

        # TODO バックグランド
        bg = Image.new("RGB", (self.__width, self.__height), (0, 0, 0))
        # 牌の幅
        tile_w = random.randint(int(self.__width/use_tile_quantity)-5, \
                                int(self.__width/use_tile_quantity))
        tile_h = int(tile_w*self.__w_h_rate)

        for tile_index, tile in enumerate(use_tiles):
            # 一つ目の牌を置く座標決定
            if tile_index == 0:
                x = random.randint(0, int(self.__width - (tile_w*use_tile_quantity)))
                y = random.randint(0, int(self.__height - tile_h))
            else:
                # ごちゃごちゃに描画
                if scatter:
                    pass
                # 揃えて描画
                else:
                    x = tile_w+x+1

            # 縮尺合わせる
            tile_img = Image.open(tile_dataset_path+"/"+tile+".jpg")
            # 牌の大きさを変更
            tile_resize = tile_img.resize((tile_w, tile_h))
            # 牌の大きさ分ずらす
            bg.paste(tile_resize, (x, y))
            # 牌の位置情報
            rectangle = [x, y, x+tile_w, y+tile_h]
            # クラス
            tile_class = onehot(tile)
            # 牌の位置情報を追加
            tile_info_.append(rectangle+tile_class)
        tile_info[img_name] = np.array(tile_info_)
        bg.save(self.__save_dir_path+'/'+img_name)
        return tile_info



