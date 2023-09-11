from sqlalchemy import Column, DateTime, String, Integer, Boolean, func, ForeignKey
# from sqlalchemy.orm import relationship
from database import Base


class Share(Base):
    __tablename__ = 'share'

    # Primary Key
    item_id = Column(String, primary_key=True, comment='要分帳的項目編號')
    share_user = Column(String, ForeignKey('users.user_id'), primary_key=True, comment='付款者(此人應為此筆消費付款給代墊者)')

    advance_user = Column(String, ForeignKey('advance.advance_user'), comment='為此筆消費預先墊付者(可能不止人)')
    share_price = Column(Integer, nullable=False, default=0, comment='應付款金額')
    is_paid = Column(Boolean, default=False, comment='是否已付款')
    created_time = Column(DateTime, default=func.now(), comment='建立時間')