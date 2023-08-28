from linebot import LineBotApi, WebhookHandler  #連接Line Bot的兩個函數
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent, TextMessage, FollowEvent, JoinEvent, TextSendMessage)
# from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, 
#                             StickerSendMessage, ImageSendMessage, LocationSendMessage, FlexSendMessage,
#                             TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackAction,
#                             PostbackEvent, QuickReplyButton, QuickReply, ConfirmTemplate, ButtonsTemplate,
#                             MessageAction)


#取得這個Lint Bot的訪問全限，取得路徑：Basic Setting -> Channel Secret
ChannelSecret = '810d353ee2085438f1bd57484ab8de89'
#調用Line Bot的Messagr API，取得路徑：Messaging API -> Channel access token
ChannelAccessToken = 'k6lNLdluZ7iQNGc4bgfhK5Aj7eoVUF7HsPqjYYDUv/yirvy59vs5sjlWJ7h4M/L3xRryRnKFzrGtMSLYSPpxPPGq1zIBpet5EkFF2iN1vYg3z/apw3TvShB+jWARRLJivsRx8a0I/Tlmq7CasOESqAdB04t89/1O/w1cDnyilFU='

handler = WebhookHandler(ChannelSecret)
line_bot_api = LineBotApi(ChannelAccessToken)