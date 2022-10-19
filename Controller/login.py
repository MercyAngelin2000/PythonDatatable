
from fastapi import status, Depends,HTTPException,APIRouter
from sqlalchemy .orm import Session
from Database.database import get_db
from Model import login
from Schema import schema

router = APIRouter()

@router.post("/samplogin")
def loginfuc(data:schema.login,db:Session = Depends(get_db)):
    msg = db.query(login.loginClass).filter(login.loginClass.email == data.email).first()
    if msg:
        return msg
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid")