# ロボットシステム学2020 課題2
## 動作環境
|||
|:--:|:--:|
|Raspberry Pi|Raspberry Pi 3 Model B+|
|OS| Ubuntu20.04|

## インストール手順
```
$ git clone https://github.com/kengo-0805/mypkg.git
$ cd mypkg

```

## 実行
```
端末1$ roscore
端末2$ cd scripts
端末2$ chmod +x count.py    
端末3$ cd scripts
端末3$ chmod +x twice.py
端末3$ rosrun mypkg twice.py
端末2$ rosrun mypkg count.py

```
## 動作説明
### count.py
数字をカウントしていき，1~100までの数字の中で  
3の倍数では"うんこ"  
3が付く数字では"💩💩💩💩💩"  
それ以外の数字では"💩"と出力されます．  


### teice.py
count.pyの数字を2倍した数が出力されます．  
count.pyの数字が1~100までの中で25の倍数の時,
（twice.pyにおける50の倍数）"💩"をたくさん出します．

世界のナ○アツ うんこverのようなイメージです．
## デモ動画
https://youtu.be/ZuXSZTRc-7w