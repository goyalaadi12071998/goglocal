from .models import Post

def create_post(payload, user_id):
    new_post = Post(
        content=payload.get("content"),
        user_id=user_id
    )
    new_post.save()
    return new_post
