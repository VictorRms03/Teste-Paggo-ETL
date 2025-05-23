from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@fonte-db:5432/fonte_db";

engine = create_engine(DATABASE_URL);
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine);