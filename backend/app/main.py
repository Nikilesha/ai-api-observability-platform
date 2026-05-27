from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.logging import logger
from app.db.deps import get_db
from app.services.log_service import save_log


app = FastAPI()

@app.get("/")
def root(db: Session = Depends(get_db)):
    save_log(db, "INFO", "Root endpoint called")
    logger.info("Root endpoint called")
    return {"message": "API Running"}

@app.get("/health")
def health(db: Session = Depends(get_db)):
    save_log(db, "INFO", "Health check endpoint called")
    logger.info("Health check endpoint called")
    return {"status": "healthy"}
