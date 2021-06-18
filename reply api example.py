from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('Line Bot 的 Channel access token')
handler = WebhookHandler('Line Bot 的 Channel secret')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):                             #根據使用者傳的訊息決定回覆內容(message)
    if event.message.text == '你好':
        message = TextSendMessage(text='hello')        
    elif  event.message.text == '圖片':
        message = ImageSendMessage(original_content_url='圖片網址', preview_image_url='圖片網址')
        
    line_bot_api.reply_message(event.reply_token, message)   #執行回覆的動作

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)