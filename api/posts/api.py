from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .schemas import PostSchemaIn, NotFoundSchema,PostSchemaOut
from .models import Posts
from typing import List


api = NinjaAPI()

@api.get("/test")
def test(request):
    return {"message":"aoabaaa"}

@api.post("/create-post")
def create_post(request, payload: PostSchemaIn):
    post = Posts.objects.create(**payload.dict())
    return {"post": post}

@api.get("/post/{post_id}", response=PostSchemaOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    return post

@api.get("/posts", response=List[PostSchemaOut])
def posts(request):
    posts = Posts.objects.all()
    return posts

@api.patch("post/{post_id}")
def update_post(request, post_id: int, payload: PostSchemaIn):
    post = get_object_or_404(Posts, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return {"success": "post updated successfully"}

@api.delete("/post/{post_id}")
def delete_post(request, post_id:int):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return {"success": "post updated successfully"}