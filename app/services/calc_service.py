def calculate_bending_capacity(wy_cm3: float, fy_mpa: float) -> float:
    # Convert cm3 → m3
    wy_m3 = wy_cm3 * 1e-6

    # Convert MPa → Pa
    fy_pa = fy_mpa * 1e6

    # Moment capacity (Nm)
    m_r = wy_m3 * fy_pa

    # Convert Nm → kNm
    return m_r / 1000


def calculate_deflection(load_kN: float, length_m: float, e_mpa: float, iy_cm4: float) -> float:
    # Convert kN → N
    load_n = load_kN * 1000

    # Convert MPa → Pa
    e_pa = e_mpa * 1e6

    # Convert cm4 → m4
    iy_m4 = iy_cm4 * 1e-8

    # δ = P L^3 / (48 E I)
    delta_m = (load_n * length_m**3) / (48 * e_pa * iy_m4)

    # Convert m → mm
    return delta_m * 1000
