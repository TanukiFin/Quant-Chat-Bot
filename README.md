# Quant-Chat-Bot

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Create-Line-Bot-from-Line">Create Line Bot from Line</a></li>
    <li><a href="#Strategy">Strategy</a></li>
    <li><a href="#Create-Database-by-MSSQL">Create Database by MSSQL</a></li>
    <li><a href="#Upload-to-Heroku">Upload to Heroku</a></li>
    <li><a href="#Files-description">Files description</a></li>
    <li><a href="#...">...</a></li>
    <li><a href="#...">...</a></li>
    <li><a href="#...">...</a></li>
  </ol>
</details>

**Push API 簡單範例**

 ```
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import *
line_bot_api = LineBotApi(' Line Bot 的 Channel access token ')
user_id = '使用者的 ID '
line_bot_api.push_message( user_id, TextSendMessage(text='Hello World!') )
print('...End')
 ```
 
**Reply API 簡單範例**

[reply api example.py](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/reply%20api%20example.py)


<!-- Create Line Bot from Line -->
## Create Line Bot from Line

<!-- Strategy -->
## Strategy

<!-- Create Database by MSSQL -->
## Create Database by MSSQL

<!-- Upload to Heroku -->
## Upload to Heroku

Procfile:告訴 Heroku 我們的應用程式是哪種類型的應用程式

requirements.txt:告訴 Heroku 需要安裝那些套件

runtime.txt:告訴 Heroku 我們要用哪種版本的 Python (非必要)

參考 : https://ithelp.ithome.com.tw/articles/10217350


<!-- Files description -->
## Files description

1. Stock stg.py

3. app.py 

  * 功用：部署到Heroku，以連接Line Bot，隨時待命，若使用者主動傳訊息，則會根據程式內容回覆。
  
  * 使用情境：
   
    1. 使用者加入好友：後臺獲得使用者的ID，並存到資料庫（然而因Heroku IP是浮動的，我無法連接資料庫）
    2. 使用者想查詢今日推薦的股票列表：從資料庫抓資料並傳送（一樣資料庫問題）



3. Daily push.py
  * 功用：每日主動傳送推薦的股票列表給使用者
