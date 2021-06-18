# Quant-Chat-Bot



<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Create-Line-Bot-from-Line">Create Line Bot from Line</a></li>
    <li><a href="#Strategy">Strategy</a></li>
    <li><a href="#Create-Database-by-MSSQL">Create Database by MSSQL</a></li>
    <li><a href="#Files-description">Files description</a></li>
    <li><a href="#Upload-to-Heroku">Upload to Heroku</a></li>
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

Line developers(官網):https://developers.line.biz/zh-hant/  

LINE BOT到資料視覺化：賴田捕手系列 第 10 篇 (創建 Line Bot):https://ithelp.ithome.com.tw/articles/10216620 

<details close="close">
  <summary>主要會用到的功能(截圖)</summary>
  <ol>
    <img src="https://i.imgur.com/VkxMjQ9.png" width="50%" height="50%">
    <li>Channel Secret</a></li>
    <li>user ID</a></li>
    <img src="https://i.imgur.com/CUjeAl6.png" width="90%" height="90%">
    <li>Webhook URL</a></li>
    <li>Channel access token</a></li>
  </ol>
</details>






<!-- Strategy -->
## Strategy



<!-- Create Database by MSSQL -->
## Create Database by MSSQL
MSSQL = SQL Server = Microsoft SQL Server

### Create Instance(執行個體)



https://www.youtube.com/watch?v=uMY2rgoPHag

https://www.youtube.com/watch?v=nvetGjSXeu8

### 設定可連結的伺服器

https://dotblogs.com.tw/Mickey/2016/12/04/194101

### 用 pymssql 連接

 ```
 import pymssql  
 conn = pymssql.connect(server='伺服器IP，根據上面教學，就是自己的IP V4', user='sa', password='yourpassword', database='UserList')
 ```
 
### 資料表預覽
<details close="close">
  <summary>程式會用到的資料表形式</summary>
  <ol>
    <li>UserList</a></li>
    
```
     	ID		Name	0	1	2
0	u3f83uhd	Emery	0	1	0
1	bsbw4gwe	Sandy	1	0	1
2	svadvvw		Kevin	1	0	1
3	g43egsde	Ken	1	0	1
4	fsavsv		Jack	1	0	1
```

   <li>StrategyList</a></li>

```
     	StrategyName	Description			Parameter
0	BBAND		今日股價由下而上 穿過下緣         BBANDS(df,timeperiod=20,nbdevup=1.0,nbdevdn=1....
1	RSI		RSI小於30，處於超賣區            RSI(df,timeperiod=14) ...
2	MACD		快線向上突破慢線                 MACD(df,fastperiod=12,slowperiod=26,signalperi...
```
     
   <li>TodaySignal</a></li>
    
 ```
	StockSymbol	StockName IndustryType	0	1	2
0	1101	台泥	  水泥工業	0	0	0
1	1102	亞泥	  水泥工業	0	0	0
2	1103	嘉泥	  水泥工業	0	0	0
3	1104	環泥	  水泥工業	0	0	0
4	1108	幸福	  水泥工業	0	0	0
...	...	...	...	...	...	...
948	9944	新麗	  其他業	        0       0       0
949	9945	潤泰新	  其他業	        0       0       0
950	9946	三發地產	  建材營造業	0       0       0
951	9955	佳龍	  其他業	        0       0       0
952	9958	世紀鋼	  鋼鐵工業       0       0       0
 ```
  說明:UserList與TodaySignal的欄位0、1、2，對應StrategyList的index，也就是BBAND、RSI、MACD策略。
  
  UserList每列為一個使用者，若一位使用者在欄位0，數值為1，代表他關注此BBAND策略；數值為0，代表不關注，其他策略同理。
 
  TodaySignal每列為一檔標的，若一檔標的在欄位0，數值為1，代表今日他觸發了BBAND的進場條件，應該買進；數值為0，代表沒觸發，其他策略同理。
 
   </ol>
</details>
 

<!-- Files description -->
## Files description

1. [Stock stg.py](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/stock%20stg.ipynb)

3. [app.py](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/UploadtoHeroku/app.py)

  * 功用：部署到Heroku，以連接Line Bot，隨時待命，若使用者主動傳訊息，則會根據程式內容回覆。
  
  * 使用情境：
   
    1. 使用者加入好友：後臺獲得使用者的ID，並存到資料庫（然而因Heroku IP是浮動的，我無法連接資料庫）
    2. 使用者想查詢今日推薦的股票列表：從資料庫抓資料並傳送（一樣資料庫問題）



3. [push msg.py](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/push%20msg.ipynb)
  * 功用：每日主動傳送推薦的股票列表給使用者




<!-- Upload to Heroku -->
## Upload to Heroku

LINE BOT到資料視覺化：賴田捕手系列 第 10 篇 (創建Heroku):https://ithelp.ithome.com.tw/articles/10216620 ，應該就能弄好Git、Heroku帳號。

LINE BOT到資料視覺化：賴田捕手系列 第 11 篇 (上傳程式碼到 Heroku):https://ithelp.ithome.com.tw/articles/10216620 ，最後應該就能部署好Line Bot，並且有回覆。

[Procfile](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/UploadtoHeroku/Procfile)　告訴 Heroku 我們的應用程式是哪種類型的應用程式

[requirements.txt](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/UploadtoHeroku/requirements.txt)　告訴 Heroku 需要安裝那些套件

[runtime.txt](https://github.com/TanukiFin/Quant-Chat-Bot/blob/main/UploadtoHeroku/runtime.txt)　告訴 Heroku 我們要用哪種版本的 Python (非必要)

上傳SOP
1. 從要上傳的資料夾打開CMD

```
D:\Users\UploadtoHeroku> 
```

2.  依序輸入
```
heroku login                         # 登入Heroku
git init
heroku git:remote -a ABC             # 將 ABC 改成 Heroku上app的名字
git add .                            # 先準備好清單，請 Git 推，所有檔案都推
git commit -am "註解自由打"
git push -f heroku master            # -f 代表不管版本強制上傳
```



