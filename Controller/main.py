from fastapi import FastAPI
from Model import schoolProfile
from Database.database import engine
from fastapi.middleware.cors import CORSMiddleware
from Controller import login,sclprofile,userProfile, register

# schoolProfile.Base.metadata.create_all(bind=engine)
schoolProfile.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(login.router)
app.include_router(sclprofile.router)
app.include_router(register.router)
app.include_router(userProfile.router)

origins = [
    "http://localhost:4200",
    "http://localhost:3000/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)