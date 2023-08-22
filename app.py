from flask import Flask, request, abort

from line_bot_api import *


app = Flask(__name__)

@app.route("/callback", methods = ['POST'])
def callback():
    signature = request.headers["X-Line-Signature"]

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret")
        abort(400)

    return 'OK'

# 初始化事件處理器(也就是每次加入LineBot時做的事情，包含封鎖及解封)
@handler.add(FollowEvent)
def handle_follow(event):

    # LineBot加入不同的環境(群組or好友)時的狀況
    if event.source.type == 'group':
        
        # 加入群組時的回復內容
        msg = '''歡迎加入群組'''    #這段要改，只是我目前懶得想歡迎詞
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )

    elif event.source.type == 'user':
        
        # 加入好友時的回復內容
        msg = '''歡迎加入好友'''    #這段要改，只是我目前懶得想歡迎詞
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )


# 文字訊息處理器(每次收到文字訊息時的動作)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    pass



if __name__ == '__main__':
    app.run()