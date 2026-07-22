from pydantic import BaseModel

class BendingRequest(BaseModel):
    wy_cm3: float
    fy_mpa: float

class BendingResponse(BaseModel):
    moment_capacity_kNm: float

class DeflectionRequest(BaseModel):
    load_kN: float
    length_m: float
    e_mpa: float
    iy_cm4: float

class DeflectionResponse(BaseModel):
    deflection_mm: float
