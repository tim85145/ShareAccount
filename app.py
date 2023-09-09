from flask import Flask, request, abort

from line_bot_api import *
from share_account import *
from database import init_db


print('11111111111111111111111111111111111111111111')
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
    
    # 加入好友時的回復內容
    msg = '''歡迎加入好友'''    #這段要改，只是我目前懶得想歡迎詞
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )

@handler.add(JoinEvent)
def handle_join(event):

    # 加入群組時的回復內容
    msg = '''歡迎加入群組'''    #這段要改，只是我目前懶得想歡迎詞
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )


# 文字訊息處理器(每次收到文字訊息時的動作)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()
    if message_text == '~開始分帳~':
        msg = '請告訴我要分帳的有哪些人。'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )
            
    elif '要分帳的人有: ' in message_text:
        if event.source.type == 'user':
            share_list = get_share_member_from_line_user(message_text)
            
            print(str(share_list))

        elif event.source.type == 'group':
            get_share_member_from_line_group(event)
    
    elif message_text == '~有哪些功能~':
        print('****************************************')
        list_all_function(event)

@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    if data.get('action') == 'item_price':
        get_item_price(event)


if __name__ == '__main__':
    init_db()
    app.run()