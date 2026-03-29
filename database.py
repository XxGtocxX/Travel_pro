from sqlalchemy import Column, Integer, String, Float, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List, Dict

Base = declarative_base()

class Flight(Base):
    """SQLAlchemy model for flights."""
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    price = Column(Float)
    seats_available = Column(Integer)
    is_direct = Column(Boolean, default=True)

class Hotel(Base):
    """SQLAlchemy model for hotels."""
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    name = Column(String)
    price_per_night = Column(Float)
    rating = Column(Float)

DATABASE_URL = "sqlite:///./travel_pro_v2.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initializes the database by dropping and recreating all tables."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def bulk_insert_data(flights: List[Dict], hotels: List[Dict]):
    """
    Bulk inserts flight and hotel data for performance.
    
    Args:
        flights: List of dictionaries representing flight entries.
        hotels: List of dictionaries representing hotel entries.
    """
    db = SessionLocal()
    try:
        db.bulk_insert_mappings(Flight, flights)
        db.bulk_insert_mappings(Hotel, hotels)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
