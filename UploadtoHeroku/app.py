# 先在要上傳的資料夾(uptoheroku)打開CMD

# heroku login
# git init
# heroku git:remote -a quant-line-bot  # heroku上app的名字

# git add .
# git commit -am "註解自由打"
# git push -f heroku master            # -f 代表不管版本強制上傳

# git pull --rebase                    # 若上傳失敗 http://hk.uwenku.com/question/p-siaorkgw-ya.html

# webhook網址 https://quant-line-bot.herokuapp.com/callback

# 教學網站 https://ithelp.ithome.com.tw/articles/10196250
#          https://ithelp.ithome.com.tw/articles/10217350
#          https://developers.line.biz/zh-hant/docs/messaging-api/building-sample-bot-with-heroku/#deploy-the-echo-sample-bot

from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import *

import os
import pymssql

def save_user(user_id):
    profile = line_bot_api.get_profile(event.source.user_id)
    name = profile.display_name
    
    conn = pymssql.connect(host='192.168.137.1',user='sa',password='linebot',database='QuantLineBot',charset='utf8')
    cursor = conn.cursor()
    df_user = pd.read_sql('select * from UserList', conn)
    
    sql = """
          INSERT INTO UserList (ID,Name,[0],[1],[2]) 
          VALUES(?,?,?,?,?)
        """
    cursor.execute(sql, user_id, name, '0', '0', '0').rowcount
    conn.commit()

    
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('wqi+ZR1fhdrF7YO24rw3dpZQwhEGg0wL4wGLiUaJOHd5k5mveO0Q8zX/oUCuvcYYvxQkgMdk58EV+DuXDI8WOIs8BFYXsI3TDR+WJUsEoIeyl/UIDfui919HAw68jeqBQTAV5AMEcZA7l3oYWWsSzwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9695c5fed987c95e049053444eb097f9')


# 收訊息的部分
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 追蹤
@handler.add(FollowEvent)
def handle_follow(event):
    print("in Follow")
    text_msg = "BBAND布林通道策略:今日股價由下而上 穿過下緣 \n RSI策略:RSI小於30，處於超賣區 \n MACD策略:快線向上突破慢線"            
    line_bot_api.reply_message( event.reply_token, TextSendMessage(text=text_msg)
    )



# 回覆訊息的部分 Reply
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    
    try:
        #關鍵字判斷
        if event.message.text == "嗨":         # 使用者傳的訊息=event.message.text
            text_msg =  event.message.text     # 重複使用者傳的訊息
            
        elif event.message.text == "說明": 
            text_msg = "這是一個傳送交易訊號機器人"  
            
        elif event.message.text == "ID": 
            text_msg = user_id
            # save_user(user_id)               #儲存使用者ID到資料庫，這裡因為資料庫IP問題，無法使用
            
    except Exception as e:
        text_msg = str(e)
        
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_msg))   #＜--執行回覆！！    

    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
