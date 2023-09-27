from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from datetime import date

from .schemas import PostSchemaIn, NotFoundSchema, PostSchemaOut, UpdatePostSchema
from .models import Posts

router = Router()


@router.get("/test")
def test(request):
    return {"message": "aoabaaa"}


@router.post("/create-post")
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


@router.get("/{post_id}", response=PostSchemaOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    return post


@router.get("/all_posts", response=List[PostSchemaOut])
def posts(request):
    posts = Posts.objects.all()
    return posts


@router.patch("/update_post/{post_id}")
def update_post(request, post_id: int, payload: UpdatePostSchema):
    post = get_object_or_404(Posts, id=post_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(post, attr, value)
    post.save()
    return {"success": "post updated successfully"}


@router.delete("/delete_post/{post_id}")
def delete_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return {"success": "post deleted successfully"}
