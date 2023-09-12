from urllib.parse import parse_qsl, quote

from models.user import Users
from models.advance import Advance
from models.share import Share
from database import db_session
from line_bot_api import *


def get_or_create_user(user_id):
    user = db_session.query(Users).filter_by(user_id=user_id).first()
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

def get_item_price(event):
    pass
    # message_text = str(event.message.text).lower().split(' ')
    # item = message_text[0]
    # price = message_text[1]


# 單人現在這

def list_all_function(event):
    functions = {'分帳功能':'開始分帳'}
    pre_message = quote('要分帳的人有: ')
    uri_base_id = quote(base_id)
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
                        "uri": f"line://oaMessage/{uri_base_id}/{pre_message}"
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

def get_share_member_from_line_user(message_text):
    share_list = message_text.split(' ')
    
    if share_list[1] == '':
        return []
    
    for user_id in share_list:
        get_or_create_user(user_id)

    return share_list[1:len(share_list)]

def print_share_member_list(event, list=[]):

    pre_message = quote('要分帳的人有: ')
    uri_base_id = quote(base_id)
    name_list_component = []

    for x in range(len(list)):
        index = f'{x}. '
        name = list[x]

        bbl_row = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": index,
                "flex": 1,
                "color": "#5B5B5B"
            },
            {
                "type": "text",
                "text": name,
                "flex": 5,
                "color": "#5B5B5B"
            }
            ]
        }

        name_list_component.append(bbl_row)

    bubble = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "分帳人員如下：",
                    "size": "xl",
                    "weight": "bold"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": name_list_component
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "繼續增加",
                "uri": f"line://oaMessage/{uri_base_id}/{pre_message}"
                },
                "height": "sm"
            },
            {
                "type": "button",
                "action": {
                "type": "postback",
                "label": "action",
                "data": "item_price"
                },
                "height": "sm"
            }
            ]
        }
    }
    
    flex_message = FlexSendMessage(
        alt_text='以下為要分帳的人員名單',
        contents=bubble)
    
    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])
