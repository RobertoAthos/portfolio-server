from ninja import Schema
from datetime import date
from typing import Optional
from pydantic import BaseModel

class PostSchemaIn(Schema):
    title: str
    subtitle: str
    content: str
    date: Optional[date] = None

class PostSchemaOut(Schema):
    title: str
    subtitle: str
    content: str
    date: date

class UpdatePostSchema(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    content: Optional[str] = None
    date: Optional[date] = None
    
class NotFoundSchema(Schema):
    message: str