from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List


from database import Base, engine, SessionLocal
import models, schemas, crud
from telegram_bot import send_incident_notification


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Incident Service")


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/incidents/", response_model=schemas.Incident)
async def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    db_incident = crud.create_incident(db, incident)
    await send_incident_notification(db_incident)
    return db_incident


@app.get("/incidents/", response_model=List[schemas.Incident])
def get_incidents(status: str = None, db: Session = Depends(get_db)):
    return crud.get_incidents(db, status=status)


@app.patch("/incidents/{incident_id}", response_model=schemas.Incident)
def update_status(incident_id: int, update_data: schemas.IncidentUpdate, db: Session = Depends(get_db)):
    incident = crud.update_incident_status(db, incident_id, update_data.status)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

