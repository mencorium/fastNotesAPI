from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, remindersCRUD

router = APIRouter()


@router.post("/", response_model=schemas.ReminderRead)
def create_reminder(reminder: schemas.ReminderCreate, db: Session = Depends(database.get_db)):
    return remindersCRUD.create_reminder(db, reminder)


@router.get("/", response_model=List[schemas.ReminderRead])
def read_reminders(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return remindersCRUD.get_reminders(db, skip=skip, limit=limit)


@router.get("/{reminder_id}", response_model=schemas.ReminderRead)
def read_reminder(reminder_id: int, db: Session = Depends(database.get_db)):
    reminder = remindersCRUD.get_reminder(db, reminder_id)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return reminder


@router.delete("/{reminder_id}", response_model=schemas.ReminderRead)
def delete_reminder(reminder_id: int, db: Session = Depends(database.get_db)):
    reminder = remindersCRUD.delete_reminder(db, reminder_id)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return reminder
