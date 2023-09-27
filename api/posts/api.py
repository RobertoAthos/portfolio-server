from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from typing import List
from datetime import date

from .schemas import PostSchemaIn, NotFoundSchema, PostSchemaOut, UpdatePostSchema
from .models import Posts

api = NinjaAPI()


@api.get("/test")
def test(request):
    return {"message": "aoabaaa"}


@api.post("/create-post")
def create_post(request, payload: PostSchemaIn):
    payload.date = date.today()
    post = Posts.objects.create(**payload.dict())
    post_data = {
        "id": post.id,
        "title": post.title,
        "subtitle": post.subtitle,
        "content": post.content,
        "date": post.date.strftime("%Y-%m-%d") if post.date else None,
    }
    return {"post": post_data}


@api.get("/post/{post_id}", response=PostSchemaOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    return post


@api.get("/posts", response=List[PostSchemaOut])
def posts(request):
    posts = Posts.objects.all()
    return posts


@api.patch("/update_post/{post_id}")
def update_post(request, post_id: int, payload: UpdatePostSchema):
    post = get_object_or_404(Posts, id=post_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(post, attr, value)
    post.save()
    return {"success": "post updated successfully"}


@api.delete("/delete_post/{post_id}")
def delete_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return {"success": "post deleted successfully"}
