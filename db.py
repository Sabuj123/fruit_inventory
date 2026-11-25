from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://fruit_v7kw_user:SEgBPEDxnoHOAIaUscdY0uyOvj8B4U56@dpg-dc3bbtu8bjmc73f6l6dg-a.virginia-postgres.render.com/fruit_v7kw"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
