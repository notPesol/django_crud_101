from .models import User

def to_dict_user(user: User) -> dict:
    return {
        "id": user.pk,
        "username": user.username,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }