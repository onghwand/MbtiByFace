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
# import cv2
import face_recognition as fr
import urllib.request as urllib
from matplotlib import pyplot as plt
import heapq
@app.post("/celebrities/top3/", response_model=list[schemas.Celebrity])
def read_top3(new_face_img: schemas.faceRequest, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
    
    plt.rcParams["figure.figsize"] = (1,1)
    
    # 이미지에서 얼굴 분리 
    celeb_faces = [] 
    for celeb in celebrities:
        celeb = fr.load_image_file(urllib.urlopen(celeb.image_url))
        top, right, bottom, left = fr.face_locations(celeb)[0]
        face_image = celeb[top:bottom, left:right]
        celeb_faces.append(face_image)
    
    # 사용자의 얼굴과 유사도 비교
    new_face_img = fr.load_image_file(urllib.urlopen(new_face_img.image_url))
    top, right, bottom, left = fr.face_locations(new_face_img)[0]
    new_face = new_face_img[top:bottom, left:right]
    enc_new_face = fr.face_encodings(new_face)
    
    for face in celeb_faces:
        enc_face = fr.face_encodings(face)
        distance = fr.face_distance(enc_face, enc_new_face[0])
        print(distance)
        # plt.title("distance: ", distance)
        # plt.imshow(face)
        # plt.show()

    # heapq 이용해서 top3 추출 후 return
     
    return celebrities
