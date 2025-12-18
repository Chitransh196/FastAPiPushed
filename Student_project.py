from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey, select
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker
from datetime import date
engine = create_engine(
    "postgresql://postgres:Radheradhe1@localhost:5432/student_department_clg",
    echo=True
)
with engine.connect() as conn:
    print(
        "✅ Connected to database:",
        conn.exec_driver_sql("SELECT current_database()").scalar()
    )

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base =declarative_base()
