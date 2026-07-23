import pytest
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(".env.test")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Shared in-memory SQLite
TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:?cache=shared"

test_engine = create_engine(
    TEST_DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)

# 1. IMPORT MAIN FIRST — this initializes the app correctly
from app.main import app

# 2. NOW import router dependency
from app.routers.member_router import get_db as member_get_db

# 3. Override dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[member_get_db] = override_get_db

# 4. Import Base AFTER main is loaded
from app.db.base import Base

@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)