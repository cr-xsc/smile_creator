# smile_creator

## デモ動画
![smile_creator](https://github.com/user-attachments/assets/fe0fca9a-33d3-499c-8b9e-09b607ac0d71)


[動画リンク](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## 目次
- [動作概要](https://github.com/cr-xsc/smile_creator/blob/main/README.jp.md#%E5%8B%95%E4%BD%9C%E6%A6%82%E8%A6%81)
- [前提とする環境](https://github.com/cr-xsc/smile_creator/blob/main/README.jp.md#%E5%89%8D%E6%8F%90%E3%81%A8%E3%81%99%E3%82%8B%E7%92%B0%E5%A2%83)
- [インストール方法](https://github.com/cr-xsc/smile_creator/blob/main/README.jp.md#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%96%B9%E6%B3%95)
- [実行手順](https://github.com/cr-xsc/smile_creator/blob/main/README.jp.md#%E5%AE%9F%E8%A1%8C%E6%89%8B%E9%A0%86)


## 動作概要
Jetson nanoに接続した USBウェブカメラ または CSIカメラの映像から人の正面の顔を検出し、   
リアルタイムで、笑顔の検出をおこないます。        
笑顔でない場合は検出した顔の上に笑顔のイラストを貼り付けます。     



## 前提とする環境

- NVIDIA Jetson Nano 開発者キット
- USB ウェブカメラ または Raspberry Pi カメラモジュール V2
- NVIDIA JetPack 4.6.1 以降


## インストール方法
ファイルのダウンロード
   ```
   $ git clone https://github.com/CosmorootMcs/smile_creator
   ```
環境のインストール
   ```
   $ pip3 install -r requirements.txt
   ```

## 実行手順

カメラの番号を確認してメモを取ります
   ```
   $ ls -la /dev/video*
   ```
ダウンロードしたフォルダに移動します
   ```
   $ cd smile_creator
   ```
下記コマンドでプログラムを実行します  カメラ番号はメモしたものを使用してください  
プログラムを終了する場合はQキーを押してください

   ```
   $ python3 smile_creator.py [--camera CAMERA_NUM]
                              [--csi]
                              [-h] 
                         
     optional arguments:
       -c CAMERA_NUM, --camera CAMERA_NUM
                          camera number
       --csi              use CSI camera
       -h, --help         show this help message and exit
   ```

コマンドを実行すると、カメラの映像が出力され  
カメラに顔が映ると、笑顔の検出し、笑顔でない場合は笑顔の画像を顔に貼り付けます。

![398385607-0e53c046-e2a7-47f8-9328-ee58f4d02827](https://github.com/user-attachments/assets/1e8b42a4-6437-4cd4-abf6-f4f3394b7554)

#### オプション
ヘルプ画面を表示する
   ```
   -h, --help
   ```

CSIカメラを使用する場合はこのオプションを追加する
   ```
   --csi
   ```

使用するカメラの番号を指定
   ```
   --camera CAMERA_NUM
   ```
#### コマンド例
csiカメラ
   ```
   $ python3 eye_mosaic.py --csi
   ```
video1のカメラを使用
   ```
   $ python3 eye_mosaic.py --camera 1
   ```


