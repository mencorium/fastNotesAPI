from fastapi import FastAPI
from .database import Base, engine
from .routers import api_router

# Ensure tables exist
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(title="Notepad API Gateway")

# Register the gateway router (with versioning)
app.include_router(api_router)
