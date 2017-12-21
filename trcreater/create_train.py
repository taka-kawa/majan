import random
import numpy as np
import cv2
import pickle
import os
import re

from imgproc import ImageProcessing


class TrainImages:
    def __init__(self, tile_datasets, save_dir, pickle_name="train_data.pickle"):
        """
        @param tile_datasets:
            ラベル(牌単体で写っている画像)のディレクトリのパスのリスト
            色々な牌のラベル画像を用意することで学習能力を高める
            例:
            ["./tile_image1", "./hoge/tile_image2",...]

            tile_image:ファイル名がその画像の牌になっているファイルがまとまっているディレクトリパス
                    |- m*.jpg:マンズの*
                    |- p*.jpg:筒子の*
                    |- s*.jpg:ソウズの*
                    |- (e,s,w,n):(東、南、西、北)
                    |- haku.jpg:白
                    |- hatsu.jpg:發
                    |- chun.jpg:中
        @param save_dir:訓練画像を保存するディレクトリのパス
        """
        self.__tile_datasets = tile_datasets
        self.__save_dir = save_dir
        self.__pickle_name = pickle_name
        self.__pr_img = ImageProcessing(self.__save_dir)
        # 下記の変数を最終的にピックル化して保存
        self.__train_img_info = {}


    def __judge_pickle(self):
        """
        直下に学習データpickleがあるかどうか確認

        return:
            pickleの有無
        """
        file_ = os.listdir("./")
        regex = re.compile(self.__pickle_name)
        for file_name in file_:
            if re.search(regex, file_name):
                return True
        return False


    def __decide_tiles(self, use_tile_quantity, target_tile_index, isMix=False):
        """
        訓練画像に使用する牌の決定
        @param use_tile_quantity:訓練に使用する牌の数
        @param target_tile_index:使用する牌の種類(tile_datasetsに渡したリスト番号指定)
        @param isMix:使用する牌の種類をごちゃ混ぜにする(Option)

        return:[使用する牌のリスト]
            例:["m1", "s4", "haku", "n"]
        """
        use_tile_dir_path = self.__tile_datasets[target_tile_index]
        tiles = [tile_name for tile_name in os.listdir(use_tile_dir_path) if re.search(r'(.jpg)+$', tile_name)]
        use_tiles = [use_tile.replace('.jpg', '') for use_tile in random.sample(tiles, use_tile_quantity)]
        return use_tiles


    def create_train_images(self, create_quantity=3, combination_range=[7,14], tile_variety=None):
        """
        訓練画像を作成する
        @param create_quantity:作成する訓練画像の数
        @param combination_range:訓練画像に用いる牌の数の幅
        @param tile_variety:使用する牌の種類(tile_datasetsに渡したリスト番号指定)
        """
        # pickleのロード
        isPickle = self.__judge_pickle()
        if isPickle:
            with open(self.__pickle_name, 'rb') as f:
                pickle_tmp = pickle.load(f)
                self.__train_img_info = pickle_tmp
        # print(self.__train_img_info)

        # 指定がない場合全てで画像生成
        if tile_variety is None:
            tile_variety = [i for i in range(len(self.__tile_datasets))]

        for target_tile_index in tile_variety:
            # 指定された量の画像を生成する。
            for created_count in range(create_quantity):
                # 画像に使用する牌の数をランダムに決定
                use_tile_quantity = random.randint(*combination_range)
                # 使用する牌の決定
                use_tiles = self.__decide_tiles(use_tile_quantity, target_tile_index)
                # 画像の加工および保存
                created_train_img_info = self.__pr_img.process_image(use_tiles, self.__tile_datasets[target_tile_index])
                tr_img_name = list(created_train_img_info.keys())[0]
                print("{}:success save".format(tr_img_name))
                self.__train_img_info[tr_img_name] = list(created_train_img_info.values())
        # 訓練画像の保存ディレクトリにpickleを保存
        with open("train_data.pickle", mode='wb') as f:
            pickle.dump(self.__train_img_info, f)


if __name__ == "__main__":
    tile_datasets = ["tile_image"]
    tr_img = TrainImages(tile_datasets, "train_image")
    tr_img.create_train_images()















