from urllib.parse import parse_qsl

from line_bot_api import *


def get_group_members_ids(group_id):
    try:
        members = line_bot_api.get_group_members_ids(group_id)
        return members
    except LineBotApiError as e:
        print(f'LineBotApiError: {e}')
        return None

def group_share(event):
    group_id = event.source.group_id
    member_ids = get_group_members_ids(group_id)
    if member_ids:
        print('群組成員的用戶 ID 列表: ')
        for member_id in member_ids:
            print(f'User ID: {member_id}')
    else:
        print('無法取得群組成員的ID列榜表')

def user_share(event):
    pass