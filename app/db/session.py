import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


host = os.environ.get("POSTGRES_HOST", 'localhost')
port = os.environ.get("POSTGRES_PORT", 5432)
user = os.environ.get("POSTGRES_USER", "postgres")
password = os.environ.get("POSTGRES_PASSWORD", "admin")
db = os.environ.get("POSTGRES_DB", "postgres")
dbtype = "postgresql"
# postgresql://user:pass@localhost/dbname

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
