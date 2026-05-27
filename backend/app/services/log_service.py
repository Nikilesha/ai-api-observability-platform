from sqlalchemy.orm import Session
from app.models.logs import Log

def save_log(db: Session, level: str, message: str):

    log = Log(
        level=level,
        message=message
    )

    db.add(log)
    db.commit()