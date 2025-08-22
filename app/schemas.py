from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# --------- Notes ---------
class NoteBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None  # match nullable=True in DB


class NoteCreate(NoteBase):
    pass  # client does not send id/created_at/updated_at


class NoteRead(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# --------- Reminders ---------
class ReminderBase(BaseModel):
    message: str
    due_date: datetime


class ReminderCreate(ReminderBase):
    pass  # client does not send id, created_at, or completed


class ReminderRead(ReminderBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
