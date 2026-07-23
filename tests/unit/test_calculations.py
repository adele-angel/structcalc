from app.services.calc_service import (
    calculate_bending_capacity,
    calculate_deflection,
)

def test_bending_capacity():
    wy_cm3 = 85.7
    fy_mpa = 235

    result = calculate_bending_capacity(wy_cm3, fy_mpa)

    # Expected: wy_m3 = 85.7e-6, fy_pa = 235e6
    # M = wy_m3 * fy_pa = 85.7e-6 * 235e6 = 20139.5 Nm = 20.1395 kNm
    assert round(result, 2) == 20.14


def test_deflection():
    load_kN = 5
    length_m = 4
    e_mpa = 210000
    iy_cm4 = 857

    result = calculate_deflection(load_kN, length_m, e_mpa, iy_cm4)

    # Just check it's positive and reasonable
    assert result > 0
    assert result < 50  # mm
