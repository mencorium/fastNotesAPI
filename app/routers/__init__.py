from fastapi import APIRouter
from . import notes, reminders

# This is the gateway router
api_router = APIRouter(prefix="/api/v1")

# Attach feature routers
api_router.include_router(notes.router, prefix="/notes", tags=["Notes"])
api_router.include_router(reminders.router, prefix="/reminders", tags=["Reminders"])
