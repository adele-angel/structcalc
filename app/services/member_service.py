from typing import List
from app.models.member import MemberModel

members_db: List[MemberModel] = []

def create_member(member: MemberModel) -> MemberModel:
    members_db.append(member)
    return member

def list_members() -> List[MemberModel]:
    return members_db
