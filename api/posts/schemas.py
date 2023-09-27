from ninja import Schema
from datetime import date


class PostSchemaIn(Schema):
    title: str
    subtitle: str
    content: str
    date: date = None

class PostSchemaOut(Schema):
    title: str
    subtitle: str
    content: str
    date: date

class NotFoundSchema(Schema):
    message: str