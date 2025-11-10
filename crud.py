from sqlalchemy.orm import Session
import models, schemas


def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(
        description=incident.description,
        status=incident.status,
        source=incident.source
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_incidents(db: Session, status: str = None):
    query = db.query(models.Incident)
    if status:
        query = query.filter(models.Incident.status == status)
    return query.all()


def update_incident_status(db: Session, incident_id: int, status: str):
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident:
        return None
    incident.status = status
    db.commit()
    db.refresh(incident)
    return incident

