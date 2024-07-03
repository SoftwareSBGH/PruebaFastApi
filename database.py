from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a SQL Server (reemplaza con tus propios datos)
DATABASE_URL = "mssql+pyodbc://sa:softwaresb@soportesb.ddns.net/SARESUC3?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
