import re
import uuid

from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel, EmailStr, field_validator

import settings


############################################################
# DATABASE BLOCK
############################################################

# create async engine for interaction with db
engine = create_async_engine(settings.REAL_DATABASE_URL, echo=True)

# create async session for interaction with db
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


############################################################
# BLOCK WITH DATABASE MODELS
############################################################

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    name_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)


############################################################
# BLOCK FOR INTERACTION WITH DATABASE IN BUSSINES CONTEXT
############################################################


class UserDAL:
    """Data Access Layer for operating user info"""
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
    
    async def create_user(
        self, name: str, surname: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    
############################################################
# BLOCK WITH API MODELS
############################################################


