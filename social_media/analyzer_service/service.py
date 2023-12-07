from .models import Post

def create_post(payload, user_id):
    new_post = Post(
        content=payload.get("content"),
        user_id=user_id
    )
    new_post.save()
    return {
        "id": new_post.id
    }

def get_analysis_data(post_id, user_id):
    data = Post.objects.filter(id=post_id, user_id=user_id).first()
    if data is None:
        return {}
    resp = get_analytical_data(data.content)
    return resp

def get_analytical_data(data):
    total_words = data.split(" ")
    total_len = len(total_words)
    total_alphabets = len(data)
    return {
        "total_words": total_len,
        "total_alphabets": total_alphabets
    }