from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://training_rzko_user:W3XBtJp74AwqknXbfUrf55CkrxTuNzPg@dpg-dc3b8jnavr4c73etcu6g-a.virginia-postgres.render.com/training_rzko"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
