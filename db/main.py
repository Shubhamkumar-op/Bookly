from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
# from sqlalchemy import text
from src.config import Config
from sqlmodel import text,SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


DATABASE_URL = Config.DATABASE_URL 
engine = create_async_engine(DATABASE_URL, echo=True)

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)
        
async def get_session()->AsyncSession:
    Session = sessionmaker(
        bind= engine,
        class_= AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session
