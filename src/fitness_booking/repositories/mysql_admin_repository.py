from sqlalchemy.orm import Session

from fitness_booking.models.admin_model import Admin


class MySQLAdminRepository:

    def __init__(self, db: Session):
        self.db = db


    def save(self, admin: Admin) -> Admin:
        self.db.add(admin)
        self.db.commit()
        self.db.refresh(admin)
        return admin