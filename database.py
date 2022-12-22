from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:Pokeball123456@localhost:5432/car_sharing')
engine.connect()
result = list(engine.execute("select * from car"))
# print(result)
# DeclarativeBase = declarative_base()
