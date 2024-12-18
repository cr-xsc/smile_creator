# smile_creator

## デモ動画
![smile_creator](https://user-images.githubusercontent.com/121159170/209026626-af6ddac4-ed43-4377-83d4-50c0a04528c0.gif)

[動画リンク](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## 目次
- [動作概要](https://github.com/CosmorootMcs/smile_creator#)
- [前提とする環境](https://github.com/CosmorootMcs/smile_creator#)
- [インストール方法](https://github.com/CosmorootMcs/smile_creator#)
- [実行手順](https://github.com/CosmorootMcs/smile_creator#)


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
                              [--smile]
                              [-h] 
                         
     optional arguments:
       -c CAMERA_NUM, --camera CAMERA_NUM
                          camera number
       --csi              use CSI camera
       -s, --smile        Smile detection
       -h, --help         show this help message and exit
   ```

コマンドを実行すると、カメラの映像が出力され  
カメラに顔が映ると、笑顔の検出をします。

![動画実行サンプル_600p](https://user-images.githubusercontent.com/121159170/209489999-98afaef8-1519-4682-a2f0-21c0419940a4.png)

#### オプション
ヘルプ画面を表示する
   ```
   -h, --help
   ```

CSIカメラを使用する場合はこのオプションを追加する
   ```
   --csi
   ```

笑顔検知
   ```
   -s, --smile
   ```
![笑顔検知](https://user-images.githubusercontent.com/121159170/209027050-cc40bd85-40b9-4dca-a526-306b5240bf68.png)


#### コマンド例
csiカメラ
   ```
   $ python3 eye_mosaic.py --csi -s
   ```


