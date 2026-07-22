from fastapi import APIRouter
from typing import List

from app.schemas.member import Member, MemberCreate
from app.models.member import MemberModel
from app.services.member_service import create_member, list_members

router = APIRouter()

@router.post("/members", response_model=Member)
def create_member_endpoint(member: MemberCreate):
    new_member = MemberModel(**member.model_dump())
    return create_member(new_member)

@router.get("/members", response_model=List[Member])
def list_members_endpoint():
    return list_members()
