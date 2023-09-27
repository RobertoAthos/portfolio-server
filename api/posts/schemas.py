from ninja import Schema
from datetime import date
from typing import Optional

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

class UpdatePostSchema(Schema):
    title: Optional[str]
    subtitle: Optional[str]
    content: Optional[str]
    date: Optional[date]
    
class NotFoundSchema(Schema):
    message: str