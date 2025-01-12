from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app import crud, schemas

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/", response_model=list[schemas.UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)

@router.post("/", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, user)
