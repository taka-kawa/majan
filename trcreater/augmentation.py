from PIL import Image, ImageEnhance, ImageFilter
import random
from itertools import product

# 加工を加える割合1/RATE
RATE = 3

def gaussian_noise(img):
    """
    ガウシアンノイズを付加する
    """
    img_pix = img.load()
    # 画像の幅と高さ取得
    w, h = img.size
    for x, y in product(*map(range, (w, h))):
        noised_colors = map(lambda x: random.gauss(x, random.randint(50,100)), img_pix[x, y])
        noised_colors = map(lambda x: max(0, x), map(lambda x: min(255, x), noised_colors))
        noised_colors = tuple(map(int, noised_colors))
        img_pix[x, y] = noised_colors
    return img

def augmentation(img):
    # 加工するかの判定をする関数
    do = (lambda : random.randint(1,100) % RATE == 0)()

    # コントラスト
    if do:
        contrast_converter = ImageEnhance.Contrast(img)
        img = contrast_converter.enhance(random.random())
    # 彩度
    if do:
        saturation_converter = ImageEnhance.Color(img)
        img = saturation_converter.enhance(random.random())
    # シャープネス
    if do:
        sharpness_converter = ImageEnhance.Sharpness(img)
        img = sharpness_converter.enhance(random.random())
    # 平滑化
    if do:
        img.filter(ImageFilter.GaussianBlur(random.random()*1.5))
    # ガウシアンノイズ
    if do:
        img = gaussian_noise(img)
    return img


