import os
from typing import Generator, Any

import pytest
import asyncpg
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

import settings
from main import app
from db.sessions import get_db


test_engine = create_async_engine(settings.TEST_DATABASE_URL, echo=True)

test_async_session = sessionmaker(test_engine, expire_on_commit=False, class_=AsyncSession)

