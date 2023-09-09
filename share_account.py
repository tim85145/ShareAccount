from urllib.parse import parse_qsl, quote
import requests
import webbrowser

from models.user import Users
from database import db_session
from line_bot_api import *


def get_or_create_user(user_id):
    user = db_session.query(Users).filter_by(line_id=user_id).first()
    if not user:
        try:
            profile = line_bot_api.get_profile(user_id)
        except LineBotApiError:
            user = Users(user_id=user_id, name=user_id, picture_url='')
        else:
            user = Users(user_id=user_id, name=profile.display_name, picture_url=profile.picture_url)
        finally:
            db_session.add(user)
            db_session.commit()

    return user

def get_group_members_ids(group_id):
    try:
        members = line_bot_api.get_group_members_ids(group_id)
        return members
    except LineBotApiError as e:
        print(f'LineBotApiError: {e}')
        return None

def get_share_member_from_line_group(event):
    group_id = event.source.group_id
    member_ids = get_group_members_ids(group_id)
    if member_id:
        print('群組成員的用戶 ID 列表: ')
        for member_id in member_ids:
            print(f'User ID: {member_id}')
            get_or_create_user(member_id)
    else:
        print('取得群組成員ID列表失敗!!')

def get_share_member_from_line_user(message_text):
    share_list = message_text.split(':')[1].split(' ')
    print(str(share_list))
    for user_id in share_list:
        get_or_create_user(user_id)

def get_item_price(event):
    message_text = str(event.message.text).lower().split(' ')
    item = message_text[0]
    price = message_text[1]

def list_all_function(event):
    functions = {'分帳功能':'開始分帳'}
    # base_id = '@429bgams'
    pre_message = '要分帳的人有: '
    bubbles = []

    for function in functions:
        label = functions[function]
        print(type(function))
        print(type(functions))
        print(type(label))
        
        bubble = {
            "type": "bubble",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": function,
                    "weight": "bold",
                    "size": "xl"
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "uri",
                    "label": label,
                    "uri": f"line://oaMessage/{base_id}/{pre_message}"
                    }
                }
                ],
                "flex": 0
            }
        }

        bubbles.append(bubble)
    
    flex_message = FlexSendMessage(
        alt_text='請選擇要使用的功能',
        contents={
            "type": "carousel",
            "contents": bubbles
        })

    """
    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])
"""
        
"""
# 預期能在使用者的輸入框放入一些文字
pre_text = '123測試'
encoded_message = quote(pre_text)
oa_message_uri = f'line://oaMessage/{base_id}/?{encoded_message}'
recipient_id = event.source.user_id
headers = {
    'Authorization': f'Bearer {ChannelAccessToken}'
}
payload = {
    'messages': [{'type': 'text', 'text':'觸發互動消息'}],
    'to': recipient_id,
    'notificationDisabled': False,
    'uri': oa_message_uri,
}

response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=payload)
if response.status_code == 200:
    print('互動消息已觸發成功')
else:
    print('互動消息觸發失敗: ', response.status_code, response.text)

print('===============')

url = 'https://line.me/R/oaMessage/@429bgams/要發送的訊息'
webbrowser.open(url)


response = requests.post('https://line.me/R/oaMessage/@429bgams/要發送的訊息')
if response.status_code == 200:
    print('互動消息已觸發成功')
else:
    print('互動消息觸發失敗: ', response.status_code, response.text)
print('===============....')
"""
    # message_text = str(event.message.text).lower()
    # user = get_or_create_user(event.source.user_id)
    



def get_expend_item():
    pass

