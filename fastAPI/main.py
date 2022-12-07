from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.get("/")
def index():
    return {"message": "Hello World"}

# @app.get("/celebrities/", response_model=list[schemas.Celebrity])
# def read_celebrities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     celebrities = crud.get_celebrities(db, skip=skip, limit=limit)
#     return celebrities

