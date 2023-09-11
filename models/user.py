from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = 'users'

    # Primary Key
    user_id = Column(String, primary_key=True, comment='使用者ID')

    name = Column(String, comment='使用者名稱')
    picture_url = Column(String(length=256), comment='使用者頭貼URL')
    created_time = Column(DateTime, default=func.now(), comment='使用者加入時間')

    user_advance = relationship('Advance', backref='advance')
    user_share = relationship('Share', backref='share')