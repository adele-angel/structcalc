from fastapi import APIRouter

from app.schemas.calc import (
    BendingRequest,
    BendingResponse,
    DeflectionRequest,
    DeflectionResponse,
)

from app.services.calc_service import (
    calculate_bending_capacity,
    calculate_deflection,
)

router = APIRouter()


@router.post("/calc/bending", response_model=BendingResponse)
def bending_endpoint(data: BendingRequest):
    result = calculate_bending_capacity(
        wy_cm3=data.wy_cm3,
        fy_mpa=data.fy_mpa
    )
    return BendingResponse(moment_capacity_kNm=result)


@router.post("/calc/deflection", response_model=DeflectionResponse)
def deflection_endpoint(data: DeflectionRequest):
    result = calculate_deflection(
        load_kN=data.load_kN,
        length_m=data.length_m,
        e_mpa=data.e_mpa,
        iy_cm4=data.iy_cm4
    )
    return DeflectionResponse(deflection_mm=result)
