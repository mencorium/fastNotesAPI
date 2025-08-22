from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, database, noteCRUD

router = APIRouter()


@router.post("/", response_model=schemas.NoteRead)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    return noteCRUD.create_note(db, note)


@router.get("/", response_model=List[schemas.NoteRead])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return noteCRUD.get_notes(db, skip=skip, limit=limit)


@router.get("/{note_id}", response_model=schemas.NoteRead)
def read_note(note_id: int, db: Session = Depends(database.get_db)):
    note = noteCRUD.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}", response_model=schemas.NoteRead)
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    note = noteCRUD.delete_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
