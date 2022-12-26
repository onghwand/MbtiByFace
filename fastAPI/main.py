from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends, FastAPI, File, UploadFile
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

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
import matplotlib.image as img
import numpy as np
import heapq
@app.post("/celebrities/top3/", response_model=list[schemas.Celebrity])
def read_top3(file: UploadFile, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
    
    plt.rcParams["figure.figsize"] = (1,1)
    
    # 이미지에서 얼굴 분리 
    celeb_faces = [] 
    for celeb in celebrities:
        celeb_image = fr.load_image_file(urllib.urlopen(celeb.image_url))
        top, right, bottom, left = fr.face_locations(celeb_image)[0]
        face_image = celeb_image[top:bottom, left:right]
        celeb_faces.append([face_image, celeb.id])
    
    # 사용자의 얼굴과 유사도 비교 
    encoded_img = np.fromstring(file.file.read(), dtype = np.uint8)
    new_face_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    # new_face_img = fr.load_image_file(img)
    top, right, bottom, left = fr.face_locations(new_face_img)[0]
    new_face = new_face_img[top:bottom, left:right]
    enc_new_face = fr.face_encodings(new_face)
    
    ### 여기 위에거 실행 완료되면 다음거 실행하게끔 해야함(지금 비동기라 오류나는 것 같음)
    plt.imshow(new_face)
    plt.show()
    
    # heapq 이용해서 top3 추출 후 return
    ranking = []
    for face, idx in celeb_faces:
        enc_face = fr.face_encodings(face)
        distance = fr.face_distance(enc_face, enc_new_face[0])
        print(idx, distance)
        heapq.heappush(ranking, [distance, idx])
        # plt.title("distance: ", distance)
        # plt.imshow(face)
        # plt.show()
    top3 = []    
    for _ in range(3):
        distance, idx = heapq.heappop(ranking)
        top3.append(idx)
    
    # print(top3)
    # filter 함수 만들 수 있으면 만들기(비교하기 뭐가 더 빠른지 => 최적화)
    response_dto = []
    for idx in top3:
        response_dto.append(crud.get_celebrity(db, idx))
    
    # print(response_dto)
    return response_dto

@app.post("/uploadfile/")
def create_upload(file: UploadFile):
    # new_face_img = fr.load_image_file(file)
    # top, right, bottom, left = fr.face_locations(new_face_img)[0]
    # new_face = new_face_img[top:bottom, left:right]
    encoded_img = np.fromstring(file.file.read(), dtype = np.uint8)
    img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    plt.imshow(img)
    plt.show() 
    return {"filename": file.file}