from sqlalchemy import Column, DateTime, String, Integer, Boolean, func, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Advance(Base):
    __tablename__ = 'advance'

    # Primary Key
    item_id = Column(Integer, primary_key=True, comment='要分帳的項目編號')
    advance_user = Column(String, ForeignKey('users.user_id'), primary_key=True, nullable=False, comment='為此筆消費預先墊付者(可能不止人)')
    
    group_id = Column(String, comment='項目所屬的群組(並非一定是LINE群組，亦或是分帳對象)')
    advance_price = Column(Integer, nullable=False, default=0, comment='預先墊付金額')
    is_paid = Column(Boolean, default=False, comment='是否已墊付(用於統計總分帳金額時不計算已付完的項目)')
    created_time = Column(DateTime, default=func.now(), comment='建立時間')

    advance_share = relationship('share', backref='share')