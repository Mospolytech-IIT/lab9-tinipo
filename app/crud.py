from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Post
from app.schemas import UserCreate, PostCreate

async def get_users(db: AsyncSession):
    result = await db.execute(select(User).order_by(User.id))
    return result.scalars().all()

async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_posts(db: AsyncSession):
    result = await db.execute(select(Post).order_by(Post.id))
    return result.scalars().all()

async def create_post(db: AsyncSession, post: PostCreate, user_id: int):
    new_post = Post(title=post.title, content=post.content, user_id=user_id)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post
