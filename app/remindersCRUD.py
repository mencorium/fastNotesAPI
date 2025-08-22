from sqlalchemy.orm import Session
from app import schemas, models


def create_reminder(db: Session, reminder: schemas.ReminderCreate):
    db_reminder = models.Reminder(**reminder.dict())
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

def get_reminders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Reminder).offset(skip).limit(limit).all()

def get_reminder(db: Session, reminder_id: int):
    return db.query(models.Reminder).filter(models.Reminder.id == reminder_id).first()

def delete_reminder(db: Session, reminder_id: int):
    reminder = db.query(models.Reminder).filter(models.Reminder.id == reminder_id).first()
    if reminder:
        db.delete(reminder)
        db.commit()
    return reminder