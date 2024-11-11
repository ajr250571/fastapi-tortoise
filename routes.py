# routes.py
from fastapi import APIRouter, HTTPException
from pony.orm import db_session
from models import User, Post
from schemas import UserCreate, UserResponse, PostCreate, PostResponse

router = APIRouter()


@router.get("/hello/")
def hello():
    return {"message": "Hello World"}


@router.post("/users/", response_model=UserResponse)
@db_session
def create_user(user: UserCreate):
    try:
        db_user = User(
            username=user.username,
            email=user.email
        )
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}", response_model=UserResponse)
@db_session
def get_user(user_id: int):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()


@router.post("/posts/", response_model=PostResponse)
@db_session
def create_post(author_id: int, post: PostCreate):
    user = User.get(id=author_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        db_post = Post(
            title=post.title,
            content=post.content,
            author=user
        )
        return db_post.to_dict()

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/posts/{post_id}", response_model=PostResponse)
@db_session
def get_post(post_id: int):
    post = Post.get(id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
