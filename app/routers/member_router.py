from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.member import Member, MemberCreate
from app.models.member import MemberModel
from app.services.member_service import create_member, list_members

router = APIRouter()

def get_db():
    # IMPORTANT: import SessionLocal INSIDE the function
    # so pytest can override this dependency
    from app.db.session import SessionLocal

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/members", response_model=Member)
def create_member_endpoint(member: MemberCreate, db: Session = Depends(get_db)):
    new_member = MemberModel(**member.model_dump())
    return create_member(db, new_member)


@router.get("/members", response_model=list[Member])
def list_members_endpoint(db: Session = Depends(get_db)):
    return list_members(db)
