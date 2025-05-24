from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Boolean, Text, Float

Base = declarative_base()

class MovieMetadata(Base):
    __tablename__ = "movies_metadata"
    id             = Column("id", BigInteger, primary_key=True, index=True)
    adult          = Column(Boolean)
    original_title = Column(Text)
    overview       = Column(Text)
    release_date   = Column(Text)
    popularity     = Column(Float)
    vote_average   = Column(Float)
    vote_count     = Column(Float)