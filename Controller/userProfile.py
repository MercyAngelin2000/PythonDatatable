from sqlalchemy .orm import Session
from fastapi import Depends,status,HTTPException,APIRouter
from Model import login
from Database.database import get_db


router = APIRouter()


@router.get("/userprofile/{id}")
def retrive_data(id:int,db : Session = Depends(get_db)):
    data =db.query(login.loginClass).filter(login.loginClass.id==id)
    retrieve = data.first()
    return retrieve



@router.put("/up_userprofile/{id}",status_code=status.HTTP_200_OK)
def updatepost(id:int,Post:dict,db : Session = Depends(get_db)):
    p=db.query(login.loginClass).filter(login.loginClass.id==id)
    data= p.first()
    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.delete("/del_userprofile/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id:int,db : Session = Depends(get_db)):
    p=db.query(login.loginClass).filter(login.loginClass.id== id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    p.delete(synchronize_session=False)
    db.commit()
