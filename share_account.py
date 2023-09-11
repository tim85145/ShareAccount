from urllib.parse import parse_qsl, quote

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
    pre_message = 'test'
    bubbles = []

    for function in functions:
        label = functions[function]
        
        bubble = {
            "type": "bubble",
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
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": label,
                        "uri": f"line://oaMessage/@429bgams/{pre_message}"
                    }
                }
                ]
            }
        } 

        bubbles.append(bubble)
    
    flex_message = FlexSendMessage(
        alt_text='請選擇要使用的功能',
        contents={
            "type": "carousel",
            "contents": bubbles
        })
    
    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])



def get_expend_item():
    pass

