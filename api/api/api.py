from ninja import NinjaAPI
from posts.api import router as event_post

api = NinjaAPI()


api.add_router("/posts", event_post)