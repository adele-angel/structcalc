from sqlalchemy.orm import Session
from app.models.member import MemberModel

def create_member(db: Session, member: MemberModel) -> MemberModel:
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

def list_members(db: Session):
    return db.query(MemberModel).all()
