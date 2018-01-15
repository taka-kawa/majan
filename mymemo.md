# 麻雀牌認識自動得点計算

## 手順  
### 学習
1. ラベル牌を作成  
  - 牌を一つずつ真上から撮影  
2. 学習データ作成←今  
  - ラベル牌をランダムに複数並べて学習画像とする  
3. 学習(SSD)→モデル作成  
### モデル作成後
4. 牌検出  
5. ルール適用→点計算  


## SSD

- [SSDのライブラリの使い方参考サイト](https://qiita.com/slowsingle/items/64cc927bb29a49a7af14)  

- [SSDのライブラリ](https://github.com/rykov8/ssd_keras)  



### 学習データのデータセットの形式

- pickle形式
  - 事前確率と分散？(prior_boxes_ssd300.pkl)
    - 事前確率と分散
    - priors[i] = [xmin, ymin, xmax, ymax, varxc, varyc, varw, varh]
  - 学習のデータセット(gt_pascal.pkl)
    - 画像中の物体の矩形
    - その物体のクラス

### Python Image Libraryインストール
[参考リンク](https://qiita.com/Gen6/items/a1f40c1dd6de7a13e2eb)


## 参考サイト
[OpenCV入門的](http://postd.cc/image-processing-101/)
[枠検出](http://pongsuke.hatenadiary.jp/entry/2017/05/19/171130)
[麻雀検出](http://blog.brainpad.co.jp/entry/2017/11/07/140000)



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





