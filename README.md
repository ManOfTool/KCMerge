# KCMerge

## Description

用特定排列方式組合截圖，為了更易寫艦娘攻略所做
最多二排是因為艦娘隊伍編成畫面的呈現二排就夠了

## Setup

`pip install -r requirements`

## Usage

`merger_v2.py mode src_path[ src_path ...] saved_name`

* mode: 組合模式
    * lv: 一排垂直排列
    * wv: 二排垂直排列，由左到右，由上到下
    * lh: 一排水平排列
    * wh: 二排水平排列，由左到右，由上到下
    * 不分大小寫

* src_path: 要組合的圖片或圖片所在資料夾
    * 一張以上圖片以空格分隔
    * 只檢查檔案之副檔名是否為JPEG或PNG
    * 硬要餵她非圖檔的檔案我也沒轍¯\\_(ツ)_/¯

* saved_name: 存檔名稱
    * 結果存成JPEG檔
    * 可為相對路徑或絕對路徑
    * 附檔名自己加

## TODO

* 加一點錯誤訊息

* 結合雲端平台做成網路服務，畢竟不是人人電腦都有Python環境
    * 遊戲倒了就算了，科科

# 暁の水平線に勝利を刻みなさいっ
