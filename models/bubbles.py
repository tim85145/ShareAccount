import json

class ListOfShareMember:

    main = {        
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "text",
                "text": "分帳人員名單",
                "weight": "bold",
                "size": "xl"
                },
                {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                        {
                        "type": "text",
                        "text": "1.",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                        },
                        {
                        "type": "text",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5,
                        "text": "..."
                        }
                    ]
                    }   
                ]
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
                    "label": "新增",
                    "uri": "https://linecorp.com"
                }
                },
                {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "確定",
                    "uri": "https://linecorp.com"
                }
                },
                {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "清空",
                    "uri": "https://linecorp.com"
                }
                }
            ],
            "flex": 0
        }
    }

    def __init__(self, main=main) -> json:
        self.main = main

    def add(self, name, main=main):
        lst_member = main['body']['contents'][1]['contents']
        len_lst_member = len(lst_member)
        add_model = lst_member[len_lst_member - 1]

        main['body']['contents'][1]['contents'][len_lst_member-1]['contents'][1]['text'] = name
        main['body']['contents'][1]['contents'].append(add_model)
        main['body']['contents'][1]['contents'][len_lst_member]['contents'][0]['text'] = len_lst_member