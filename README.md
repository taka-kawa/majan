# 麻雀牌認識自動得点計算

## 手順
1. ラベル牌を作成
2. 学習データ作成
3. 学習
4. 牌検出
5. ルール適用→点計算

## キーワード
- 物体検出
  1. 物体領域候補の抽出
     - スライディングウィンドウ法：時間かかる→BInarized Normed Gradients
     - 選択的検索法
  2. 物体領域候補の物体認識
     - 検出された各領域を１枚の画像と見立てて、クラス認識手法を適用
  3. 検出領域の絞り込み



## SSD

https://qiita.com/slowsingle/items/64cc927bb29a49a7af14

https://qiita.com/PonDad/items/6f9e6d9397951cadc6be

[github](https://github.com/rykov8/ssd_keras)



### 学習データのデータセットの形式

- pickle形式
  - 事前確率と分散？(prior_boxes_ssd300.pkl)
    - 事前確率と分散
    - priors[i] = [xmin, ymin, xmax, ymax, varxc, varyc, varw, varh]
  - 学習のデータセット(gt_pascal.pkl)
    - 画像中の物体の矩形
    - その物体のクラス



## 学習データ作成


### Python Image Libraryインストール
[参考リンク](https://qiita.com/Gen6/items/a1f40c1dd6de7a13e2eb)





## 参考サイト
[OpenCV入門的](http://postd.cc/image-processing-101/)
[枠検出](http://pongsuke.hatenadiary.jp/entry/2017/05/19/171130)
[麻雀検出](http://blog.brainpad.co.jp/entry/2017/11/07/140000)





