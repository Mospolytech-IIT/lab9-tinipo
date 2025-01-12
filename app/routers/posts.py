from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app import crud, schemas

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/", response_model=list[schemas.PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await crud.get_posts(db)

@router.post("/", response_model=schemas.PostResponse)
async def create_post(post: schemas.PostCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.create_post(db, post, user_id)
