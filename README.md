# RoadBike Fitting Assistant


![result](https://github.com/satodayo/RoadBikeFittingAssistant/blob/master/result/resultpic.jpg)

## How To Install

1. python3.x for Windowsをインストールしてください

https://www.python.org/downloads/


2. PowerShellで以下のコマンドを叩いてください

  ```py -m pip install -U pip```

  ```pip install requests```

  ```pip install numpy```

## Hou To Use

1. このリポジトリをダウンロードし、sourceフォルダ内に計測したい画像を入れて下さい
- ファイル名は'source.jpg'としてください
- 画像は体の**右側**が正面に来るように撮影してください
- 画像には本人以外の人物が映らないよう気を付けてください

2. PowerShell上でこのリポジトリを開いてください

3. main.pyを実行してください

ex.)

```python main.py```

4. Resultフォルダ内に測定結果が保存されます

## Result
- Elbow Angle:肘-手首, 肘-肩間の角度

- Shoulder Angle:肩-肘, 肩-尻間の角度

- Hip Angle:尻-肩, 尻-膝間の角度

- Knee Angle:膝-尻, 膝-足首間の角度

## Caution
- 多少の誤差が発生する可能性があるため、参考程度にご利用ください

**※株式会社UserLocal様の姿勢推定AI APIを利用させていただいています。**
