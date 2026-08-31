from sqlalchemy.orm import Session



class MySQLBookedSessionRepository:
    def __init__(self, db: Session):
        self.db = db