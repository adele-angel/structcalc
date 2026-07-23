import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Detect test mode
TESTING = os.getenv("PYTEST_CURRENT_TEST") is not None

if TESTING:
    # Use SQLite in-memory DB for tests
    DATABASE_URL = "sqlite+pysqlite:///:memory:"
    engine = create_engine(DATABASE_URL, echo=False)
else:
    # Use real PostgreSQL in Docker
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
