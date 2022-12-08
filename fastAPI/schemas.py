from typing import Union

from pydantic import BaseModel

class CelebrityBase(BaseModel):
    name: str
    mbti: str
    image_url: str

class CelebrityCreate(CelebrityBase):
    pass

class Celebrity(CelebrityBase):
    id: int
    
    class Config:
        orm_mode = True