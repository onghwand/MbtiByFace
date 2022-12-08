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
@app.get("/celebrities/top3", response_model=list[schemas.Celebrity])
def read_top3(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
    for celeb in celebrities:
        print(celeb.image_url, type(celeb))
    return celebrities





