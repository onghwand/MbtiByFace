from sqlalchemy.orm import Session
import models, schemas

def get_celebrity(db: Session, celebrity_id: int):
    return db.query(models.Celebrity).filter(models.Celebrity.id == celebrity_id).first()

def get_celebrities(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.Celebrity).offset(skip).limit(limit).all()

def create_celebrity(db: Session, celebrity: schemas.CelebrityCreate):
    db_celebrity = models.Celebrity(name=celebrity.name, mbti=celebrity.mbti, image_url=celebrity.image_url)
    db.add(db_celebrity)
    db.commit()
    db.refresh(db_celebrity) # refresh : 자동 생성된 pk까지 포함한 instance로 갱신
    return db_celebrity