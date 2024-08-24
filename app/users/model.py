from sqlalchemy import Column, Integer, ForeignKey, Date, Computed, String
from app.database import Base

# Users Model
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)  # Added Integer type
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)