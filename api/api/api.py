from ninja import NinjaAPI
from posts.api import router as event_post
from chat.api import router as event_chat

api = NinjaAPI()


api.add_router("/posts", event_post)
api.add_router("/chat", event_chat)