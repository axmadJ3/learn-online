from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import settings

# create async engine for interaction with db
engine = create_async_engine(settings.REAL_DATABASE_URL, echo=True)

# create async session for interaction with db
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
        