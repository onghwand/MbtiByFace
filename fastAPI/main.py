from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "Hello World"}

'''
연예인 리스트 반환
'''
@app.get("/celebrities/", response_model=list[schemas.Celebrity])
def read_celebrities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
    return celebrities

'''
임의의 사용자 사진을 받아 가장 비슷한 연예인 정보를 반환
'''
import cv2
import face_recognition as fr
import urllib.request as urllib
from matplotlib import pyplot as plt
@app.get("/celebrities/top3", response_model=list[schemas.Celebrity])
def read_top3(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
    
    plt.rcParams["figure.figsize"] = (1,1)
    celeb_images = []
    for celeb in celebrities:
        # print(celeb.image_url, type(celeb))
        response = urllib.urlopen(celeb.image_url)
        celeb_images.append(fr.load_image_file(response))
    
    celeb_faces = [] 
    for celeb in celeb_images:
        top, right, bottom, left = fr.face_locations(celeb)[0]
        face_image = celeb[top:bottom, left:right]
        
        celeb_faces.append(face_image)
    
    for face in celeb_faces:
        plt.imshow(face)
        plt.show()
    return celebrities





