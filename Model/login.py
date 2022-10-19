from sqlalchemy import Column, Integer,String,Date,BigInteger
from Database.database import Base


class loginClass(Base):
    __tablename__ = "login"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    firstname = Column(String, nullable =False)
    lastname = Column(String,nullable = False)
    phone = Column(BigInteger, nullable =False)
    email = Column(String,nullable = False, unique= True)
    dob = Column(Date, nullable = False)
    gender = Column(String,nullable = False)
    pwd = Column(String,nullable = False)
