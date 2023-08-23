from urllib.parse import parse_qsl

from line_bot_api import *


def group_share(event):
    group_id = event.source.group_id
    member_ids = line_bot_api.get_group_member_ids(group_id)
    print(member_ids)