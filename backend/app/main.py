from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text, select
from .database import SessionLocal
from typing import List
import datetime

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/data/")
def get_data(start_time: datetime.datetime, end_time: datetime.datetime, variables: List[str] = Query(...), db: Session = Depends(get_db)):

    columns = ["timestamp"] + variables
    columnsQuery = ", ".join(columns)

    query = text(f"SELECT {columnsQuery} FROM data WHERE timestamp BETWEEN :start AND :end")
    result = db.execute(query, {"start": start_time, "end": end_time}).fetchall()

    data = [dict(row._mapping) for row in result]
    return data